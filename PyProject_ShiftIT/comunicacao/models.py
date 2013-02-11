# -*- coding: utf-8 -*-
'''
Created on Jul 11, 2012

@author: Shift IT | www.shiftit.com.br
'''

from django.db                                      import models

#-----------------------------EMAIL---------------------------------------


class Contato(models.Model):
    id_contato          = models.IntegerField(max_length=3, primary_key=True, null= False, blank=True)
    nome                = models.CharField(max_length=500, verbose_name='Nome') 
    email               = models.CharField(max_length=500, verbose_name='E-mail') 
    telefone            = models.CharField(max_length=500, verbose_name='Telefone') 
    mensagem            = models.CharField(max_length=10000, verbose_name='Mensagem') 
    data                = models.DateTimeField(null= True, verbose_name='Data')
        
    class Meta:
        db_table= 'tb_contato'
        verbose_name = 'Contato'
        verbose_name_plural = 'Contato'
    
    def __unicode__(self):
        return str(self.id_contato)
    
    def save(self):  
        if self.id_contato == '' or self.id_contato== None:
            if len(Contato.objects.order_by('-id_contato')) > 0:   
                iUltimoRegistro = Contato.objects.order_by('-id_contato')[0] 
                self.id_contato= iUltimoRegistro.pk + 1
            else:
                self.id_contato= 1
        super(Contato, self).save()

