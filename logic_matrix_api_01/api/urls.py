from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('blogposts/', views.BlogPostListCreate.as_view(), name='blogposts'),
    path('blogposts/<int:pk>/', views.BlogpostRetrieveUpdateDestroy.as_view(), name='blog'),
]