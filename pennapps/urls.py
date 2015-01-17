from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pennapps.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^create$', 'tindeers.views.create', name='create'),
    url(r'^$', 'tindeers.views.main_page', name='home'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
