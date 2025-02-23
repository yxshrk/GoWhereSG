
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("createactivities", views.createactivities, name="createactivities"),
    path("productivity", views.productivity, name="productivity"),
    path("view_activity/<int:activity_id>", views.view_activity, name="view_activity"),
    path("review_personal/<int:activity_id>", views.review_personal, name="review_personal"),
    path("addremark/<int:activity_id>", views.addremark, name="addremark"),
    path("specialedit/<int:activity_id>", views.specialedit, name="specialedit"),
    path("editactivity/<int:activity_id>", views.editactivity, name="editactivity"),
    path("categories", views.categories, name="categories"),
    path("category/<str:categ>", views.category, name="category"),
    path("youritineraries", views.youritineraries, name="youritineraries"),
    path("youritinerary/<str:typeofactivity>", views.youritinerary, name="youritinerary"),
    path("addtoitinerary/<int:activity_id>", views.addtoitinerary, name="addtoitinerary"),
    path("recentlyaddeditems", views.recentlyaddeditems, name="recentlyaddeditems"),
    path("view_activitysecond/<int:activity_id>", views.view_activitysecond, name="view_activitysecond"),
    path("removefrompersonalitinerary/<int:activity_id>", views.removefrompersonalitinerary, name="removefrompersonalitinerary"),
    path("maps", views.maps, name="maps")

]
