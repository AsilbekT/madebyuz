from distutils.command.upload import upload
from email.policy import default
from pyexpat import model
from django.db import models
from django.urls import reverse
import slugify

# Create your models here.
class Blog(models.Model):
    about = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    picture = models.ImageField(upload_to="blogs/images", default='default.jpg')
    subtext = models.TextField(blank=True)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True)
    def __str__(self):
        return self.title

    @property
    def picture_url(self):
        try:
            url = self.picture.url
        except:
            url = ''
        return url
    

    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify.slugify(self.title)
        return super().save(*args, **kwargs)
