from ast import Delete
from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
import slugify
# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User,  on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField('Name', max_length=200, null=True)
    email = models.CharField('Email', max_length=200, null=True)

    def __str__(self):
        return self.name

class Catagories(models.Model):
    name = models.CharField(max_length=200)
    picture = models.ImageField(upload_to="catagories", default="default.jpg")
    slug = models.SlugField(blank=True)
    
    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify.slugify(self.name)
        return super().save(*args, **kwargs)
    def __str__(self):
        return self.name

    @property
    def product_url(self):
        try:
            url = self.picture.url
        except:
            url = ''
        return url
        
        
class Products(models.Model):
    catagory_id = models.ForeignKey(Catagories, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.IntegerField()
    picture = models.ImageField(upload_to="products")
    picture_for_mini_items = models.ImageField(upload_to="products", default='default.jpg')
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify.slugify(self.name)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return f"/{self.catagory_id.slug}/"

    @property
    def product_url(self):
        try:
            url = self.picture.url
        except:
            url = ''
        return url



class Order(models.Model):
    customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(auto_now_add=True)
    city = models.CharField(max_length=100, default='Tashkent')
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    @property
    def get_cart_total(self):
        order_items = self.orderitem_set.all()
        total = sum([item.get_total for item in order_items])
        return total


    @property
    def get_cart_items(self):
        order_items = self.orderitem_set.all()
        total = sum([item.quantity for item in order_items])
        return total

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    product = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_ended = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

    def __str__(self):
        return self.product.name


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, null=True,  on_delete=models.CASCADE)
    order = models.ForeignKey(Order, null=True,  on_delete=models.CASCADE)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address


