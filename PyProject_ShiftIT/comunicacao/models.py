# -*- coding: utf-8 -*-
'''
Created on Jul 11, 2012

@author: Shift IT | www.shiftit.com.br
'''

from django.db                                      import models

import logging

#-----------------------------EMAIL---------------------------------------

class Email(models.Model):
    nome                = models.CharField(max_length=500, verbose_name='Nome') 
    email               = models.CharField(max_length=500, verbose_name='E-mail') 
    telefone            = models.CharField(max_length=500, verbose_name='Telefone') 
    mensagem            = models.TextField(max_length=10000, verbose_name='Mensagem') 
    data                = models.DateTimeField(null= True, verbose_name='Data')
        
    class Meta:
        db_table= 'tb_email'
        verbose_name = 'Email'
        verbose_name_plural = 'Email'
    
    def __unicode__(self):
        return str(self.id)

#-----------------------------CONTATO---------------------------------------

class Contato(models.Model):
    nome                = models.CharField(max_length=500, verbose_name='Nome') 
    email               = models.CharField(max_length=500, verbose_name='E-mail') 
    telefone            = models.CharField(max_length=500, verbose_name='Telefone') 
    data                = models.DateTimeField(null= True, verbose_name='Data')
        
    class Meta:
        db_table= 'tb_contato'
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'
    
    def __unicode__(self):
        return self.nome
        
#-----------------------------PERGUNTA CONTATO---------------------------------------
        
class Pergunta_Contato(models.Model):
    pergunta            = models.TextField(max_length=500, verbose_name='Pergunta') 
        
    class Meta:
        db_table= 'tb_pergunta_contato'
        verbose_name = 'Pergunta de Contato'
        verbose_name_plural = 'Perguntas de Contato'
    
    def __unicode__(self):
        return self.pergunta
    
    def obtemPerguntaContato(self, vIDPerguntaContato):
        try:
            iPerguntaContato= Pergunta_Contato.objects.filter(id= vIDPerguntaContato)[0]
            return iPerguntaContato
        except Exception, e:
            logging.getLogger('PyProject_ShiftIT.controle').error('Nao foi possivel obtem Pergunta Contato: ' + str(e))
            return None   
        
#-----------------------------RESPOSTA CONTATO---------------------------------------
        
class Resposta_Contato(models.Model):
    pergunta            = models.ForeignKey(Pergunta_Contato, null= False, verbose_name='Pergunta')
    contato             = models.ForeignKey(Contato, null= False, verbose_name='Contato')
    resposta            = models.TextField(max_length=500, verbose_name='Resposta') 
        
    class Meta:
        db_table= 'tb_resposta_contato'
        verbose_name = 'Resposta de Contato'
        verbose_name_plural = 'Respostas de Contato'
    
    def __unicode__(self):
        return self.resposta
