from django.contrib import sitemaps
from django.urls import reverse


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return [
            'mainapp:index', 'mainapp:about', 'mainapp:contact', 'mainapp:rules',
            'blog:landing_page',
            'authentication:register',
            'my:panel',
            ]

    def location(self, item):
        return reverse(item)