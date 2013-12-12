from django.conf.urls.defaults      import patterns, include, url
from django.contrib                 import admin

from django.conf                    import settings

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    (r'^media/(.*)$', 'django.views.static.serve',
     {'document_root': settings.MEDIA_ROOT}),
    (r'^', include('flatpages.urls')),
    (r'^', include('comunicacao.urls')),
    (r'^', include('autenticacao.urls')),
    (r'^', include('bugtracker.urls')),
    url(r'^skwissh/', include('skwissh.urls')),
)
