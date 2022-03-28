from django.urls import path
from blogs import views

urlpatterns = [
    path('blogs/', views.blogs, name='blog'),
    path('blogs/<slug:slug>/', views.blog_details, name='blog_details'),
]