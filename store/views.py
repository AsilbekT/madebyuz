from itertools import product
from math import prod
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Products, Catagories, Order, OrderItem
from django.core.exceptions import ObjectDoesNotExist
import json
# Create your views here.
from .utils import cartData

def home1(request):
    data = cartData(request)
    cartItem = data['cartItems']
    order = data['order']
    items = data['items']
    catagories = Catagories.objects.all()
    clothes = catagories[4].products_set.all()
    context = {"clothes": clothes, 'catagories': catagories, 'cartItem': cartItem, 'items': items, 'order':order}
    return render(request, "home/index.html", context)



def home2(request):
    return render(request, "home/index-2.html")



def organic_food(request):
    return render(request, "organic_food/organic_food.html")


def organic_clothes(request):
    return render(request, "organic_food/organic_food.html")


def home_textile(request):
    return render(request, "home_textile/home_textile.html")


def home4(request):
    return render(request, "home/index-4.html")


def wine(request):
    return render(request, "wine/wine.html")


def about(request):
    data = cartData(request)
    cartItem = data['cartItems']
    order = data['order']
    items = data['items']
    catagories = Catagories.objects.all()
    clothes = catagories[4].products_set.all()
    context = {"clothes": clothes, 'catagories': catagories, 'cartItem': cartItem, 'items': items, 'order':order}
    return render(request, "about.html", context)


def contact(request):
    data = cartData(request)
    cartItem = data['cartItems']
    order = data['order']
    items = data['items']
    catagories = Catagories.objects.all()
    clothes = catagories[4].products_set.all()
    context = {"clothes": clothes, 'catagories': catagories, 'cartItem': cartItem, 'items': items, 'order':order}
    return render(request, "contact.html", context)






def cart(request):
    data = cartData(request)
    cartItem = data['cartItems']
    order = data['order']
    items = data['items']
    catagories = Catagories.objects.all()
    clothes = catagories[4].products_set.all()
    context = {"clothes": clothes, 'catagories': catagories, 'cartItem': cartItem, 'items': items, 'order':order}
    return render(request, "store/cart.html", context)


def checkout(request):
    data = cartData(request)
    cartItem = data['cartItems']
    order = data['order']
    items = data['items']
    catagories = Catagories.objects.all()
    clothes = catagories[4].products_set.all()
    context = {"clothes": clothes, 'catagories': catagories, 'cartItem': cartItem, 'items': items, 'order':order}
    return render(request, "store/checkout.html", context)


def shop_details(request, id):
    data = cartData(request)
    cartItem = data['cartItems']
    order = data['order']
    items = data['items']
    catagories = Catagories.objects.all()
    clothes = catagories[4].products_set.all()
    try:
        product = [i for i in items if i.product.id == id][0]
    except IndexError:
        product = Products.objects.get(id=id)
    context = {"clothes": clothes, 'catagories': catagories, 'cartItem': cartItem, 'items': items, 'order':order, 'item': product, }
    return render(request, "store/shop-details.html", context)


def shop(request):
    data = cartData(request)
    cartItem = data['cartItems']
    order = data['order']
    items = data['items']
    catagories = Catagories.objects.all()
    clothes = catagories[4].products_set.all()
    products = Products.objects.all()
    context = {"clothes": clothes, 'catagories': catagories, 'cartItem': cartItem, 'items': items, 'order':order, 'products': products}
    return render(request, "store/shop.html", context)


def update_item(request):
    data = json.loads(request.body)
    product_id = data['productId']
    action = data['action']
    customer = request.user.customer
    product = Products.objects.get(id=product_id)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    order_items, created = OrderItem.objects.get_or_create(order=order, product=product)
    if action == "add":
        order_items.quantity += 1
    elif action == "remove":
        order_items.quantity -= 1
    order_items.save()
    
    if action == "delete":
        order_items.delete()

    if order_items.quantity <= 0:
        order_items.delete()

    return JsonResponse({"data":"added"})