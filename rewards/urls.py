from django.urls import path
from . import views 
from .forms import SignupForm

from django.contrib.auth import views as authViews

urlpatterns=[
    path('signup/', views.signup, name='signup'),
   	#path('login/', authViews.LoginView.as_view(template_name='login.html'), name='login'),
   	#path('logout/', authViews.LogoutView.as_view(), {'next_page' : 'login'}, name='logout'),

    path('api/profile/',views.Profile_list.as_view()),
    path('api/image/',views.Image_list.as_view()),
    path('',views.home, name='home'),
    path(r'upload/', views.upload, name='upload'),
    path(r'search/', views.search_results, name='search_results')
]