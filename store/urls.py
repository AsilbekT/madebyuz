from django.urls import path
from store import views

urlpatterns = [
    path('', views.home1, name='home1'),
    path('home2/', views.home2, name='home2'),
    path('organic_food/', views.organic_food, name='organic_food'),
    path('home_textile/', views.home_textile, name='home_textile'),
    path('wine/', views.wine, name='wine'),
    path('home4/', views.home4, name='home4'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('shop_detail/<int:id>', views.shop_details, name='shop_details'),
    path("update_item/", views.update_item, name='update_item'),
    path('shop', views.shop, name='shop'),
]
