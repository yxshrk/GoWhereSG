from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(User)
admin.site.register(Productivity)
admin.site.register(Remarks)
admin.site.register(Itinerary)
admin.site.register(WatchList)