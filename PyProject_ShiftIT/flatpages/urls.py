from django.conf.urls.defaults  import *
from django.utils.translation   import ugettext_lazy as trans

urlpatterns= patterns('flatpages.views',
                      url('^$', 'home',
                          {'vTitulo': trans(u'Home')}, name='home'), 
                      url('^time/$', 'time',
                            {'vTitulo': trans(u'Time')}, name='time'), 
                      url('^como_fazemos/$', 'como_fazemos',
                            {'vTitulo': trans(u'Como Fazemos')}, name='como_fazemos'), 
                      url('^o_que_fazemos/$', 'o_que_fazemos',
                            {'vTitulo': trans(u'O que fazemos')}, name='o_que_fazemos'), 
                      url('^google6196345173a7df0a.html/$', 'google',
                          {'vTitulo': trans(u'Google')}, name='Google'),
                      )