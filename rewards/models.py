from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to = 'project/')
    description = models.CharField(max_length=150)
    #link

    def __str__(self):
        return self.title

class Profile(models.Model):
    profile_pic = models.ImageField(upload_to = 'profile/')
    user_bio = models.CharField(max_length=150)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    #contact_info = 
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'