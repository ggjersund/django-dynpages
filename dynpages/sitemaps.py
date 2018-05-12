from django.contrib.sitemaps import Sitemap
from . models import DynPage


class DynpageSitemap(Sitemap):
    def items(self):
        return DynPage.objects.all()
