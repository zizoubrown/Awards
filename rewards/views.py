from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile, Project

# Create your views here.
def home(request):
    return render(request, 'index.html')