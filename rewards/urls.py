from django.urls import path
from . import views

urlpatterns=[
    path('',views.home, name='home'),
    path(r'upload/', views.upload, name='upload'),
    path(r'search/', views.search_results, name='search_results')
]