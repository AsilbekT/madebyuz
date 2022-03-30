from django.urls import path
from pages import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('a/', views.a, name='a'),
]
