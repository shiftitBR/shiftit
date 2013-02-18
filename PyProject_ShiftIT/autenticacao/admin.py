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
from PyProject_ShiftIT.bugtracker.models        import Documento, Bug,\
    Estado_Bug, Pergunta_Bug, Resposta_Bug



class AdminUsuario(admin.ModelAdmin): 
    list_display    = ('get_nome',  )
    search_fields   = UserAdmin.search_fields
    exclude         = ('last_login', 'date_joined', 'is_superuser', 'user_permissions', 
                       'is_staff', 'slug', 'is_active', 'groups') 
    
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
    list_display    = ('pergunta', 'contato', 'resposta', )
    search_fields   = ('resposta', 'pergunta.pergunta', 'contato.first_name', 'contato.last_name')
    exclude         = ('id_resposta_contato',) 
    
class AdminDocumento(admin.ModelAdmin): 
    list_display    = ('usuario', 'assunto', 'arquivo' )
    search_fields   = ('assunto', 'usuario.first_name', 'usuario.last_name')
    exclude         = ('id_documento',) 
    
    
class AdminBug(admin.ModelAdmin): 
    list_display    = ('usuario', 'tipo_prioridade', 'descricao', 'nome_contato', 'email_contato', 'telefone_contato', 'imagem', 'data' )
    search_fields   = ('descricao', 'usuario.first_name', 'usuario.last_name', 'nome_contato', 'email_contato', 'telefone_contato', 'tipo_prioridade.descricao')
    exclude         = ('id_bug',) 
    
class AdminEstadoBug(admin.ModelAdmin): 
    list_display    = ('bug', 'tipo_estado', 'comentario', 'data' )
    search_fields   = ('bug.descricao', 'bug.nome_contato', 'comentario', 'tipo_estado.descricao')
    exclude         = ('id_estado_bug',) 
    
class AdminPerguntaBug(admin.ModelAdmin): 
    list_display    = ('pergunta',  )
    search_fields   = ('pergunta', )
    exclude         = ('id_pergunta_bug',) 
    
class AdminRespostaBug(admin.ModelAdmin): 
    list_display    = ('pergunta', 'bug', 'resposta', )
    search_fields   = ('resposta', 'pergunta.pergunta', 'bug.descricao')
    exclude         = ('id_resposta_bug',) 
    
admin.site.unregister(User)
admin.site.unregister(Site)
admin.site.unregister(Group)
admin.site.register(Usuario, AdminUsuario)
admin.site.register(Contato, AdminContato)
admin.site.register(Pergunta_Contato, AdminPerguntaContato)
admin.site.register(Resposta_Contato, AdminRespostaContato)
admin.site.register(Documento, AdminDocumento)
admin.site.register(Bug, AdminBug)
admin.site.register(Estado_Bug, AdminEstadoBug)
admin.site.register(Pergunta_Bug, AdminPerguntaBug)
admin.site.register(Resposta_Bug, AdminRespostaBug)
