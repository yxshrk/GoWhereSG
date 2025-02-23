from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.contrib.auth.decorators import login_required
import datetime
import json


superuser = User.objects.get(is_superuser=True)

def index(request):
    superuser = User.objects.get(is_superuser=True)
    return render(request, "network/index.html", {
        "superuser": superuser
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

@login_required(login_url='/login')
def createactivities(request):
    if request.method == "POST":
        activity = Productivity()
        activity.activity_title = request.POST.get("title")
        activity.activity_description = request.POST.get("description")
        activity.category = request.POST.get("category").upper()
        activity.link = request.POST.get("link")
        activity.estimatedcost = request.POST.get("cost")
        activity.activity_datetime = request.POST.get("date")
        activity.save()

        return render(request, "network/createactivities.html")

    else:
        return render(request, "network/createactivities.html")

@csrf_exempt
@login_required(login_url='/login')
def productivity(request):
    if request.method == "POST":
        data = json.loads(request.body)
        title = data.get("title")
        content = data.get("content")
        category = data.get("category")
        cost = data.get("cost")
        date = data.get("date")

        obj = Productivity()
        obj.user = request.user.username
        obj.activity_title = title.upper()
        obj.activity_datetime = date
        obj.activity_description = content
        obj.category = category.upper()
        obj.estimatedcost = cost
        obj.save()

        ball = WatchList()
        ball.user = request.user.username
        ball.activityid = obj.id
        ball.save()

        activities = Productivity.objects.all()

        return render(request, "network/productivity.html", {
        "activites": activities

        })

    else:
        activities = Productivity.objects.all()
        return render(request, "network/productivity.html", {
            "activities": activities
        })




@login_required(login_url='/login')
def view_activity(request, activity_id):
    superuser = User.objects.get(is_superuser=True)
    remarks = Remarks.objects.filter(activityid=activity_id).order_by('-timestamp')
    if request.method == "POST":
        activity = Productivity.objects.get(id=activity_id)

        return render(request, "network/view_activity.html" , {
            "activity": activity,
            "remarks": remarks,
            "superuser": superuser
        })
    else:
        activity = Productivity.objects.get(id=activity_id)
        return render(request, "network/view_activity.html" , {
            "activity": activity,
            "remarks": remarks,
            "superuser":superuser
        })

@login_required(login_url='/login')
def review_personal(request, activity_id):
    remarks = Remarks.objects.filter(activityid=activity_id).order_by('-timestamp')
    if request.method == "POST":
        activity = Productivity.objects.get(id=activity_id)

        return render(request, "network/review_personal.html" , {
            "activity": activity,
            "remarks": remarks,
            "superuser": superuser
        })
    else:
        activity = Productivity.objects.get(id=activity_id)
        return render(request, "network/review_personal.html" , {
            "activity": activity,
            "remarks": remarks,
            "superuser": superuser
        })

@login_required(login_url='/login')
def view_activitysecond(request, activity_id):
    remarks = Remarks.objects.filter(activityid=activity_id).order_by('-timestamp')
    if request.method == "POST":
        activity = Productivity.objects.get(id=activity_id)

        return render(request, "network/view_activity2.html" , {
            "activity": activity,
            "remarks": remarks,
            "superuser": superuser
        })
    else:
        activity = Productivity.objects.get(id=activity_id)
        return render(request, "network/view_activity2.html" , {
            "activity": activity,
            "remarks": remarks,
            "superuser": superuser
        })


@login_required(login_url='/login')
def addremark(request, activity_id):
    obj = Remarks()
    obj.content = request.POST.get("remark")
    obj.activityid = activity_id
    obj.save()

    remarks = Remarks.objects.filter(activityid=activity_id).order_by('-timestamp')
    activity = Productivity.objects.get(id=activity_id)
    #added = Watchlist.objects.filter(listingid=product_id, user=request.user.username)
    return render(request, "network/view_activity2.html", {
        "activity": activity,
        "remarks": remarks
    })





@login_required(login_url='/login')
def editactivity(request, activity_id):
    remarks = Remarks.objects.filter(activityid=activity_id).order_by('-timestamp')
    if request.method == "POST":

        activity = Productivity.objects.get(id=activity_id)
        activity.user = request.user.username
        activity.activity_title = request.POST.get("title")
        activity.activity_description = request.POST.get("description")
        activity.category = request.POST.get("category").upper()
        activity.estimatedcost = request.POST.get("cost")
        activity.activity_datetime = request.POST.get("date")
        activity.save()


        activity = Productivity.objects.get(id=activity_id)

        return render(request, "network/review_personal.html", {
        "activity": activity,
        "remarks": remarks

        })

    else:
        activity = Productivity.objects.get(id=numb)

        return render(request, "network/review_personal.html", {
        "activity": activity,
        "remarks": remarks

        })

@login_required(login_url='/login')
def recentlyaddeditems(request):
    lst = WatchList.objects.filter(user=request.user.username)
    activity_list = []
    if lst:
        for item in lst:
            activity = Productivity.objects.get(id=item.activityid)
            activity_list.append(activity)

    paginator = Paginator(activity_list, 10)
    page = request.GET.get('page')
    return render(request, "network/recentlyaddeditems.html", {
        "activity_list": activity_list
    })

@login_required(login_url='/login')
def addtoitinerary(request, activity_id):
    #activity = Productivity.objects.get(id=activity_id)
    remarks = Remarks.objects.filter(activityid=activity_id).order_by('-timestamp')
    items = WatchList.objects.filter(user=request.user.username)
    added_activities = []
    for item in items:
            activity = Productivity.objects.get(id=item.activityid)
            added_activities.append(activity)

    obj = WatchList.objects.filter(user=request.user.username, activityid=activity_id)
    if obj:
        obj.delete()
        added = WatchList.objects.filter(activityid=activity_id, user=request.user.username)

        return HttpResponseRedirect(reverse("recentlyaddeditems"))
    else:
        obj = WatchList()
        obj.user = request.user.username
        obj.activityid = activity_id
        obj.save()

        added = WatchList.objects.filter(activityid=activity_id, user=request.user.username)

        return HttpResponseRedirect(reverse("recentlyaddeditems"))




@login_required(login_url='/login')
def categories(request):
    return render(request, "network/categories.html")


@login_required(login_url='/login')
def category(request, categ):
    categorised_activities = Productivity.objects.filter(category=categ).order_by('-timestamp')
    items = WatchList.objects.filter(user=request.user.username)
    added_activities = []
    if items is not None:
        for item in items:
            activity = Productivity.objects.get(id=item.activityid)
            added_activities.append(activity)



    paginator = Paginator(categorised_activities, 10)
    page = request.GET.get('page')
    return render(request, "network/category.html", {
        "activities": paginator.get_page(page),
        "categ": categ
    })


@login_required(login_url='/login')
def youritineraries(request):
    return render(request, "network/itineraries.html")

@login_required(login_url='/login')
def youritinerary(request, typeofactivity):
    activities = Productivity.objects.filter(user=request.user.username, category=typeofactivity).order_by('-timestamp')
    paginator = Paginator(activities, 10)
    page = request.GET.get('page')
    return render(request, "network/itinerary.html", {
        "activities": paginator.get_page(page),
        "typeofactivity": typeofactivity
    })

@login_required(login_url='/login')
def removefrompersonalitinerary(request, activity_id):
    activity = Productivity.objects.get(id=activity_id)
    activity.user = None
    activity.save()

    categ = activity.category
    activities = Productivity.objects.filter(user=request.user.username, category=categ).order_by('-timestamp')
    paginator = Paginator(activities, 10)
    page = request.GET.get('page')
    return render(request, "network/itinerary.html", {
        "activities": paginator.get_page(page),
        "typeofactivity": categ
    })

@login_required(login_url='/login')
def maps(request):
    superuser = User.objects.get(is_superuser=True)
    return render(request, "network/maps.html", {
        "superuser": superuser
    })





@login_required(login_url='/login')
def specialedit(request, activity_id):
    if request.method == "POST":

        activity = Productivity.objects.get(id=activity_id)
        activity.user = request.user.username
        activity.activity_title = request.POST.get("title")
        activity.activity_description = request.POST.get("description")
        activity.category = request.POST.get("category").upper()
        activity.estimatedcost = request.POST.get("cost")
        activity.activity_datetime = request.POST.get("date")
        activity.save()

        categ = activity.category
        activities = Productivity.objects.filter(user=request.user.username, category=categ).order_by('-timestamp')
        paginator = Paginator(activities, 10)
        page = request.GET.get('page')
        return render(request, "network/itinerary.html", {
            "activities": paginator.get_page(page),
            "typeofactivity": categ
        })

    else:
        remarks = Remarks.objects.filter(activityid=activity_id).order_by('-timestamp')
        activity = Productivity.objects.get(id=activity_id)

        return render(request, "network/review_personal.html", {
        "activity": activity,
        "remarks": remarks

        })



