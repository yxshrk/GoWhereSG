from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Productivity(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.CharField(max_length=64, null=True)
    activity_title = models.CharField(max_length=1024)
    activity_datetime = models.CharField(max_length=1024)
    activity_description = models.TextField(default=None, null=True)
    category = models.CharField(max_length=1024, null=True)
    link = models.CharField(max_length=1024, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    estimatedcost = models.CharField(max_length=64)


class Itinerary(models.Model):
    activityid = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Remarks(models.Model):
    content = models.CharField(max_length=1024)
    activityid = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)


class WatchList(models.Model):
    user = models.CharField(max_length=64)
    activityid = models.IntegerField(null=True)
    category = models.CharField(max_length=1024, null=True)



