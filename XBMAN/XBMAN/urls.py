from django.conf.urls import include, url
from django.contrib import admin
from asset import rest_urls
urlpatterns = [
    # Examples:
    # url(r'^$', 'XBMAN.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(rest_urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
