from django.contrib import admin
from django.urls import path, include
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
)

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),  # By convention, use '<name>-home' to prevent collision
    path('about/', views.about, name='blog-about'),  # localhost/about
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),


]

# When we use CBV, we can't use them directly in urls. But, django has a method avaliable that does this
# `as_view()`
# <app>/<model>_<viewtype>.html
# We can use variables in our uRL paths with the <type:var> syntax.
