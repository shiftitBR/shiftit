# -*- coding: utf-8 -*-
'''
Created on Jul 11, 2012

@author: Shift IT | www.shiftit.com.br
'''

from django.db                                          import models
from django.contrib.auth.models                         import User
from django.db.models                                   import signals
from django.template.defaultfilters                     import slugify
from django.core.urlresolvers                           import reverse

import logging
       
        
#---------------------------USUARIO -----------------------------------    
    
class Usuario(User):
    cnpj            = models.CharField(max_length=60, null= True, blank=True, verbose_name='CNPJ')
    razao_social    = models.CharField(max_length=500, null= True, blank=True, verbose_name='Razão Social')
    nome_fantasia   = models.CharField(max_length=500, null= True, blank=True, verbose_name='Nome Fantasia')
    endereco        = models.CharField(max_length=500, null= True, blank=True, verbose_name='Endereço')
    cidade          = models.CharField(max_length=100, null= True, blank=True, verbose_name='Cidade')
    uf              = models.CharField(max_length=100, null= True, blank=True, verbose_name='Estado')
    nome_responsavel= models.CharField(max_length=200, null= True, blank=True, verbose_name='Responsável')
    telefone        = models.CharField(max_length=60, null= True, blank=True, verbose_name='Telefone')
    slug            = models.SlugField(max_length=500, blank=True, unique=True)
    
    class Meta:
        db_table= 'tb_usuario'
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
    
    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)
    
    def get_absolute_url(self):
        return reverse('autenticacao.views.perfil', kwargs={'slug': self.slug})
    
    def save(self):  
        if self.username == '':
            if len(User.objects.order_by('-id')) > 0:   
                iUltimoRegistro = User.objects.order_by('-id')[0] 
                self.id= iUltimoRegistro.pk + 1
            else:
                self.id= 1
        super(Usuario, self).save()  
        
    def possuiUsuario(self, vIDUser):
        try:
            if len(Usuario.objects.filter(id= vIDUser)) > 0:
                return True
            else: 
                return False
        except Exception, e:
            logging.getLogger('PyProject_ShiftIT.controle').error('Nao foi possui Usuario: ' + str(e))
            return None   
        
    def obtemUsuario(self, vIDUsuario):
        try:
            iUsuario= Usuario.objects.filter(id= vIDUsuario)[0]
            return iUsuario
        except:
            return None   
    
    def obtemUsuarioSlug(self, vSlug):
        try:
            iUsuario= Usuario.objects.filter(slug= vSlug)[0]
            return iUsuario
        except Exception, e:
            logging.getLogger('PyProject_ShiftIT.controle').error('Nao foi possivel obtem Usuario Slug: ' + str(e))
            return None 
        
def usuario_pre_save(signal, instance, sender, **kwargs):
    """Este signal gera um slug automaticamente. Ele verifica se ja existe um
    artigo com o mesmo slug e acrescenta um numero ao final para evitar
    duplicidade"""
    try:
        slug = slugify(instance.nome_fantasia)
        novo_slug = slug
        contador = 0
    except Exception, e:
        slug = slugify(instance.id)
        novo_slug = slug
        contador = 0
        logging.getLogger('PyProject_ShiftIT.controle').error('Nao foi possivel usuario_pre_save: ' + str(e))
        
    
    while Usuario.objects.filter(slug=novo_slug).exclude(id=instance.id).count() > 0:
        contador += 1
        novo_slug = '%s-%d'%(slug, contador)

    instance.slug = novo_slug
    

signals.pre_save.connect(usuario_pre_save, sender=Usuario)

    
