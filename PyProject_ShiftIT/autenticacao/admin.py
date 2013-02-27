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

class DocumentoInLine(admin.StackedInline): 
    model           = Documento
    list_display    = ('usuario', 'assunto', 'arquivo' )
    search_fields   = ('assunto', 'usuario.first_name', 'usuario.last_name')
    exclude         = ('id_documento',) 
    verbose_name    = 'Documento'
    verbose_name_plural = 'Documentos'
    extra           = 0

class AdminUsuario(admin.ModelAdmin): 
    inlines         = (DocumentoInLine,)
    fieldsets       = (
        (None, {
            'fields': ('username', 'first_name', 'last_name', 'cnpj', 'razao_social', 'nome_fantasia', 
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
#    readonly_fields = ('id_resposta_contato',)
#    exclude         = ('id_resposta_contato',) 
#    verbose_name    = 'Resposta de Contato'
#    verbose_name_plural = 'Respostas de Contato'
    
class AdminContato(admin.ModelAdmin): 
    inlines         = (RepostaContatoInline,)
    list_display    = ('nome', 'email', 'telefone', 'data', )
    search_fields   = ('nome', 'email', 'telefone', 'data', )
    exclude         = ('id_contato',) 
        
class AdminPerguntaContato(admin.ModelAdmin): 
    list_display    = ('pergunta',  )
    search_fields   = ('pergunta', )
    exclude         = ('id_pergunta_contato',) 
    
class RespostaBugInLIne(admin.StackedInline): 
    model           = Resposta_Bug
    list_display    = ('pergunta', 'bug', 'resposta', )
    search_fields   = ('resposta', 'pergunta.pergunta', 'bug.descricao')
    extra           = 0
#    exclude         = ('id_resposta_bug',) 
#    verbose_name    = 'Resposta de Bug'
#    verbose_name_plural = 'Respostas de Bug'
    
class EstadoBugInLine(admin.StackedInline): 
    model           = Estado_Bug
    list_display    = ('bug', 'tipo_estado', 'comentario', 'data' )
    search_fields   = ('bug.descricao', 'bug.nome_contato', 'comentario', 'tipo_estado.descricao')
    extra           = 0
#    exclude         = ('id_estado_bug',) 
#    verbose_name    = 'Estado de Bug'
#    verbose_name_plural = 'Estados de Bug'
    
class AdminBug(admin.ModelAdmin): 
    inlines         = (RespostaBugInLIne, EstadoBugInLine, )
    list_display    = ('usuario', 'tipo_prioridade', 'descricao', 'nome_contato', 'email_contato', 
                       'telefone_contato', 'imagem', 'data' )
    search_fields   = ('descricao', 'usuario.first_name', 'usuario.last_name', 'nome_contato', 
                       'email_contato', 'telefone_contato', 'tipo_prioridade.descricao')
    exclude         = ('id_bug',) 
    
class AdminPerguntaBug(admin.ModelAdmin): 
    list_display    = ('pergunta',  )
    search_fields   = ('pergunta', )
    exclude         = ('id_pergunta_bug',) 
    
admin.site.unregister(User)
admin.site.unregister(Site)
admin.site.unregister(Group)
admin.site.register(Usuario, AdminUsuario)
admin.site.register(Contato, AdminContato)
admin.site.register(Pergunta_Contato, AdminPerguntaContato)
admin.site.register(Bug, AdminBug)
admin.site.register(Pergunta_Bug, AdminPerguntaBug)
#admin.site.register(Resposta_Contato, AdminRespostaContato)
#admin.site.register(Documento, AdminDocumento)
#admin.site.register(Estado_Bug, AdminEstadoBug)
#admin.site.register(Resposta_Bug, AdminRespostaBug)