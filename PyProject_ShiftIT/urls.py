from django.conf.urls.defaults      import patterns, include, url
from django.contrib                 import admin

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    (r'^', include('flatpages.urls')),
    (r'^', include('comunicacao.urls')),
    (r'^', include('autenticacao.urls')),
    (r'^', include('bugtracker.urls')),
)
