from django.contrib import admin
from .models import Profile, Image, Rating

admin.site.site_header = "Awards Admin"
admin.site.site_title = "Awards Admin Area"
admin.site.index_title = "Welcome to Awards admin"


# Register your models here.
admin.site.register(Profile)
admin.site.register(Image)
admin.site.register(Rating)