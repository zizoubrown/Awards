from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import  Profile, Image, Rating

# Create your views here.
def home(request):
    post = Project.objects.all()

    return render(request, 'index.html' ,{'post':post})

def upload(request):
    if request.method == 'POST': 
        form = PostPictureForm(request.POST, request.FILES) 
        if form.is_valid():
            post = form.save(commit=False)
            post.profile = request.user.profile
            form.save()
            return redirect('home') 
    else: 
        form = PostPictureForm() 
    return render(request, 'upload.html', {'form' : form}) 


