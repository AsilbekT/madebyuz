from django.shortcuts import render
from store.utils import cartData
from store.models import Catagories
from .models import Blog
import slugify
# Create your views here.

def blogs(request):
    data = cartData(request)
    cartItem = data['cartItems']
    order = data['order']
    items = data['items']
    blogs = Blog.objects.all()
    catagories = Catagories.objects.all()

    clothes = catagories[4].products_set.all()
    context = {"clothes": clothes, 'catagories': catagories, 'cartItem': cartItem, 'items': items, 'order':order, 'blogs': blogs}
    return render(request, "blogs/blog.html", context)


def blog_details(request, slug):
    data = cartData(request)
    cartItem = data['cartItems']
    order = data['order']
    items = data['items']
    blog = Blog.objects.get(slug=slug)
    catagories = Catagories.objects.all()
    clothes = catagories[4].products_set.all()
    context = {"clothes": clothes, 'catagories': catagories, 'cartItem': cartItem, 'items': items, 'order':order, 'blog': blog}
    return render(request, "blogs/blog-details.html", context)