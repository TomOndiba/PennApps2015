from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pennapps.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('social.apps.django_app.urls', namespace='social')),
    url(r'^create$', 'tindeers.views.create', name='create'),
    url(r'^createApi$', 'tindeers.views.create_api', name='create_api'),
    url(r'^product/(?P<vid>\d+)$', 'tindeers.views.display', name='product'),
    url(r'^$', 'tindeers.views.main_page', name='home'),
    url(r'^vote$', 'tindeers.views.vote', name='vote'),
    url(r'^aggregate/(?P<pid>\d+)$', 'tindeers.views.aggregate', name='aggregate'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
