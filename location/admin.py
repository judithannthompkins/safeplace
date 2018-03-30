from django.contrib import admin

# Register your models here.
from .models import Category, Crime, Location, LocationInstance

admin.site.register(Category)
admin.site.register(Crime)
admin.site.register(Location)
admin.site.register(LocationInstance)

