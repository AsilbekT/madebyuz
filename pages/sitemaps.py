from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    changefreq = "yearly"
    priority = 0.5
    def items(self):
        return ['about', 'contact', 'login', 'signup']
    def location(self, item):
        return reverse(item)



