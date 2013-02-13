# -*- coding: utf-8 -*-
'''
Created on Jan 17, 2012

@author: Shift IT | www.shiftit.com.br
'''

from django.contrib                             import admin
from django.contrib.auth.admin                  import UserAdmin 
from django.contrib.auth.models                 import User
from django.contrib.auth.models                 import Group
from django.contrib.sites.models                import Site

from PyProject_ShiftIT.autenticacao.models      import Usuario
from PyProject_ShiftIT.comunicacao.models       import Contato
from PyProject_ShiftIT.comunicacao.models       import Pergunta_Contato
from PyProject_ShiftIT.comunicacao.models       import Resposta_Contato


class AdminUsuario(admin.ModelAdmin): 
    list_display    = ('get_nome',  )
    search_fields   = UserAdmin.search_fields
    exclude         = ('last_login', 'date_joined', 'is_superuser', 'user_permissions', 
                       'username', 'is_staff', 'slug', 'is_active', 'groups') 
    
    def get_nome(self, obj):
        return '%s %s'%(obj.first_name, obj.last_name)
    get_nome.short_description = 'Nome'
    
class AdminContato(admin.ModelAdmin): 
    list_display    = ('nome', 'email', 'telefone', 'data', )
    search_fields   = ('nome', 'email', 'telefone', 'data', )
    exclude         = ('id_contato',) 
    
class AdminPerguntaContato(admin.ModelAdmin): 
    list_display    = ('pergunta',  )
    search_fields   = ('pergunta', )
    exclude         = ('id_pergunta_contato',) 
    
class AdminRespostaContato(admin.ModelAdmin): 
    list_display    = ('pergunta', 'contato', 'resposta' )
    search_fields   = ('resposta', 'pergunta.pergunta', 'contato.first_name', 'contato.last_name')
    exclude         = ('id_resposta_contato',) 
    
    
admin.site.unregister(User)
admin.site.unregister(Site)
admin.site.unregister(Group)
admin.site.register(Usuario, AdminUsuario)
admin.site.register(Contato, AdminContato)
admin.site.register(Pergunta_Contato, AdminPerguntaContato)
admin.site.register(Resposta_Contato, AdminRespostaContato)
