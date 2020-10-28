from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, update_session_auth_hash, login
from django.http import HttpResponse
from .models import  Profile, Image, Rating
from .forms import PostPictureForm, SignupForm

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    posts = Image.objects.all()

    return render(request, 'index.html' ,{'posts':posts})

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

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})