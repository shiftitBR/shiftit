from django.conf.urls.defaults  import *
from django.utils.translation   import ugettext_lazy as trans

urlpatterns= patterns('comunicacao.views',
                      url('^contato/$', 'contato',
                            {'vTitulo': trans(u'contato')}, name='contato'), 
                      url('^briefing/$', 'briefing',
                            {'vTitulo': trans(u'briefing')}, name='briefing'), 
                      )