from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticSitemap(Sitemap):
    changefreq = "yearly"
    priority = 1
    protocol = 'https'

    def items(self):
        return [
            'web:index',
            'web:about-us',
            'web:projects',
            'web:services-2',
            'web:blog-with-sidebar',
            'web:contact'
        ]

    def location(self, item):
        return reverse(item)
