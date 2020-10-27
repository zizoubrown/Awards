from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to = 'project/')
    description = models.CharField(max_length=150)
    #link

class Profile(models.Model):
    profile_pic = models.ImageField(upload_to = 'profile/')
    user_bio = models.CharField(max_length=150)
    project = models.ForeignKey(Profile, on_delete=models.CASCADE)
    #contact_info = 