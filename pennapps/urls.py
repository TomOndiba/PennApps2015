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
    url(r'^home$', 'tindeers.views.main_page', name='home'),
    url(r'^$', 'tindeers.views.landing', name='landing'),
    url(r'^manage/(?P<product_id>\d+)$', 'tindeers.views.feedback', name='feedback'),
    url(r'^manage$', 'tindeers.views.manage_all', name='manage_all'),
    url(r'^vote$', 'tindeers.views.vote', name='vote'),
    url(r'^aggregate/(?P<pid>\d+)$', 'tindeers.views.aggregate', name='aggregate'),
    url(r'^comment/(?P<pid>\d+)$', 'tindeers.views.comment', name='comment'),
    url(r'^explore$', 'tindeers.views.explore', name='explore'),
    url(r'^logout$', 'tindeers.views.logout_view', name='logout_view'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
