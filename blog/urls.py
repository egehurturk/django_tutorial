from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'), # By convention, use '<name>-home' to prevent collision
    path('about/', views.about, name='blog-about'), # localhost/about
    
]