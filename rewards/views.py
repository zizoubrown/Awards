from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Profile, Project

# Create your views here.
def home(request):
    post = Project.objects.all()

    return render(request, 'index.html' ,{'post':post})