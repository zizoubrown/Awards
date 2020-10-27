from django.contrib import admin
from .models import Project,Profile

admin.site.site_header = "Awards Admin"
admin.site.site_title = "Awards Admin Area"
admin.site.index_title = "Welcome to Awards admin"


# Register your models here.
admin.site.register(Project)
admin.site.register(Profile)