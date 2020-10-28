from django.urls import path
from . views import *
from .forms import SignupForm

from django.contrib.auth import views as authViews

urlpatterns=[
    path('signup/', Signup, name='signup'),
   	path('login/', authViews.LoginView.as_view(template_name='login.html'), name='login'),
   	path('logout/', authViews.LogoutView.as_view(), {'next_page' : 'login'}, name='logout'),

    path('',home, name='home'),
    path(r'upload/', upload, name='upload'),
    path(r'search/', search_results, name='search_results')
]