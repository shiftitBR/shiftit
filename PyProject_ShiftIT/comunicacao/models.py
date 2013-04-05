# -*- coding: utf-8 -*-
'''
Created on Jul 11, 2012

@author: Shift IT | www.shiftit.com.br
'''

from django.db                                      import models

import logging

#-----------------------------EMAIL---------------------------------------

class Email(models.Model):
    id_email            = models.IntegerField(max_length=3, primary_key=True, null= False, blank=True, verbose_name='ID')
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
        return str(self.id_email)
    
    def save(self):  
        if self.id_email == '' or self.id_email== None:
            if len(Email.objects.order_by('-id_email')) > 0:   
                iUltimoRegistro = Email.objects.order_by('-id_email')[0] 
                self.id_email= iUltimoRegistro.pk + 1
            else:
                self.id_email= 1
        super(Email, self).save()

#-----------------------------CONTATO---------------------------------------

class Contato(models.Model):
    id_contato          = models.IntegerField(max_length=3, primary_key=True, null= False, blank=True, verbose_name='ID')
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
    
    def save(self):  
        if self.id_contato == '' or self.id_contato== None:
            if len(Contato.objects.order_by('-id_contato')) > 0:   
                iUltimoRegistro = Contato.objects.order_by('-id_contato')[0] 
                self.id_contato= iUltimoRegistro.pk + 1
            else:
                self.id_contato= 1
        super(Contato, self).save()
        
#-----------------------------PERGUNTA CONTATO---------------------------------------
        
class Pergunta_Contato(models.Model):
    id_pergunta_contato = models.IntegerField(max_length=3, primary_key=True, null= False, blank=True, verbose_name='ID')
    pergunta            = models.CharField(max_length=500, verbose_name='Pergunta') 
        
    class Meta:
        db_table= 'tb_pergunta_contato'
        verbose_name = 'Pergunta de Contato'
        verbose_name_plural = 'Perguntas de Contato'
    
    def __unicode__(self):
        return self.pergunta
    
    def save(self):  
        if self.id_pergunta_contato == '' or self.id_pergunta_contato== None:
            if len(Pergunta_Contato.objects.order_by('-id_pergunta_contato')) > 0:   
                iUltimoRegistro = Pergunta_Contato.objects.order_by('-id_pergunta_contato')[0] 
                self.id_pergunta_contato= iUltimoRegistro.pk + 1
            else:
                self.id_pergunta_contato= 1
        super(Pergunta_Contato, self).save()
    
    def obtemPerguntaContato(self, vIDPerguntaContato):
        try:
            iPerguntaContato= Pergunta_Contato.objects.filter(id_pergunta_contato= vIDPerguntaContato)[0]
            return iPerguntaContato
        except Exception, e:
            logging.getLogger('PyProject_ShiftIT.controle').error('Nao foi possivel obtem Pergunta Contato: ' + str(e))
            return None   
        
#-----------------------------RESPOSTA CONTATO---------------------------------------
        
class Resposta_Contato(models.Model):
    id_resposta_contato = models.IntegerField(max_length=3, primary_key=True, null= False, blank=True, verbose_name='ID')
    pergunta            = models.ForeignKey(Pergunta_Contato, null= False, verbose_name='Pergunta')
    contato             = models.ForeignKey(Contato, null= False, verbose_name='Contato')
    resposta            = models.CharField(max_length=500, verbose_name='Resposta') 
        
    class Meta:
        db_table= 'tb_resposta_contato'
        verbose_name = 'Resposta de Contato'
        verbose_name_plural = 'Respostas de Contato'
    
    def __unicode__(self):
        return self.resposta
    
    def save(self):  
        if self.id_resposta_contato == '' or self.id_resposta_contato== None:
            if len(Resposta_Contato.objects.order_by('-id_resposta_contato')) > 0:   
                iUltimoRegistro = Resposta_Contato.objects.order_by('-id_resposta_contato')[0] 
                self.id_resposta_contato= iUltimoRegistro.pk + 1
            else:
                self.id_resposta_contato= 1
        super(Resposta_Contato, self).save()
