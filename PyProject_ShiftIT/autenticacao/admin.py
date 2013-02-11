# -*- coding: utf-8 -*-
'''
Created on Jan 17, 2012

@author: Shift IT
'''

from django.contrib                         import admin
from django.contrib.auth.admin              import UserAdmin 
from django.contrib.auth.models             import User
from django.contrib.auth.models             import Group
from django.contrib.sites.models            import Site

from PyProject_ShiftIT.autenticacao.models   import Usuario


class AdminUsuario(admin.ModelAdmin): 
    list_display    = ('get_nome',  )
    search_fields   = UserAdmin.search_fields
    exclude         = ('last_login', 'date_joined', 'is_superuser', 'user_permissions', 
                       'username', 'is_staff', 'slug', 'is_active', 'groups') 
    
    def get_nome(self, obj):
        return '%s %s'%(obj.first_name, obj.last_name)
    get_nome.short_description = 'Nome'

    
admin.site.unregister(User)
admin.site.unregister(Site)
admin.site.unregister(Group)
admin.site.register(Usuario, AdminUsuario)
