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

from autenticacao.models                        import Usuario
from comunicacao.models                         import Contato, Email
from comunicacao.models                         import Pergunta_Contato
from comunicacao.models                         import Resposta_Contato
from bugtracker.models                          import Documento, Bug, Estado_Bug, Pergunta_Bug, Resposta_Bug

class DocumentoInLine(admin.StackedInline): 
    model           = Documento
    list_display    = ('usuario', 'assunto', 'arquivo' )
    search_fields   = ('assunto', 'usuario.first_name', 'usuario.last_name')
    verbose_name    = 'Documento'
    verbose_name_plural = 'Documentos'
    extra           = 0

class AdminUsuario(admin.ModelAdmin): 
    inlines         = (DocumentoInLine,)
    fieldsets       = (
        (None, {
            'fields': ('username', 'first_name', 'last_name', 'password', 'cnpj', 'razao_social', 'nome_fantasia', 
                       'telefone', 'endereco', 'cidade', 'uf', 'nome_responsavel')
        }),
        ('Opções Avançadas', {
            'classes': ('collapse',),
            'fields': ('last_login', 'date_joined', 'is_superuser', 'user_permissions', 
                       'is_staff', 'slug', 'is_active', 'groups')
        }),
    )
    list_display    = ('nome_fantasia', 'nome_responsavel', 'username', 'cnpj', )
    search_fields   = UserAdmin.search_fields
    
class RepostaContatoInline(admin.StackedInline):
    model           = Resposta_Contato
    list_display    = ('pergunta', 'contato', 'resposta', )
    search_fields   = ('resposta', 'pergunta.pergunta', 'contato.first_name', 'contato.last_name')
    extra           = 0
    
class AdminContato(admin.ModelAdmin): 
    inlines         = (RepostaContatoInline,)
    list_display    = ('nome', 'email', 'telefone', 'data', )
    search_fields   = ('nome', 'email', 'telefone', 'data', )
        
class AdminPerguntaContato(admin.ModelAdmin): 
    list_display    = ('pergunta',  )
    search_fields   = ('pergunta', )
    
class RespostaBugInLIne(admin.StackedInline): 
    model           = Resposta_Bug
    list_display    = ('pergunta', 'bug', 'resposta', )
    search_fields   = ('resposta', 'pergunta.pergunta', 'bug.descricao')
    extra           = 0
    
class EstadoBugInLine(admin.StackedInline): 
    model           = Estado_Bug
    list_display    = ('bug', 'tipo_estado', 'comentario', 'data' )
    search_fields   = ('bug.descricao', 'bug.nome_contato', 'comentario', 'tipo_estado.descricao')
    extra           = 0
    
class AdminBug(admin.ModelAdmin): 
    inlines         = (RespostaBugInLIne, EstadoBugInLine, )
    list_display    = ('usuario', 'tipo_prioridade', 'descricao', 'nome_contato', 'email_contato', 
                       'telefone_contato', 'imagem', 'data' )
    search_fields   = ('descricao', 'usuario.first_name', 'usuario.last_name', 'nome_contato', 
                       'email_contato', 'telefone_contato', 'tipo_prioridade.descricao')
    
class AdminPerguntaBug(admin.ModelAdmin): 
    list_display    = ('pergunta',  )
    search_fields   = ('pergunta', )
    
class AdminEmail(admin.ModelAdmin): 
    list_display    = ('nome', 'email', 'telefone', 'mensagem', 'data')
    search_fields   = ('nome', 'email', 'telefone', 'mensagem', 'data')
    
admin.site.unregister(User)
admin.site.unregister(Site)
admin.site.unregister(Group)
admin.site.register(Usuario, AdminUsuario)
admin.site.register(Contato, AdminContato)
admin.site.register(Pergunta_Contato, AdminPerguntaContato)
admin.site.register(Bug, AdminBug)
admin.site.register(Pergunta_Bug, AdminPerguntaBug)
admin.site.register(Email, AdminEmail)
