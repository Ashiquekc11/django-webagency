from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap
from web.sitemap import StaticSitemap


sitemaps = {
    'static':StaticSitemap,
}
urlpatterns = (
    [
        path('admin/doc/',include('django.contrib.admindocs.urls')),
        path("admin/", admin.site.urls),
        path("", include("web.urls", namespace="web")),
        # path(
        #     "sitemap.xml",
        #     TemplateView.as_view(template_name="static_sitemap.xml", content_type="text/xml")),
        path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
        path(
            "robots.txt",
            TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)

admin.site.site_header = "PROJECT Administration"
admin.site.site_title = "PROJECT Admin Portal"
admin.site.index_title = "Welcome to PROJECT Admin Portal"
