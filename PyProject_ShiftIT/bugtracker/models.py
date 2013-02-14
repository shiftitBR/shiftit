# -*- coding: utf-8 -*-
'''
Created on Jul 11, 2012

@author: Shift IT | www.shiftit.com.br
'''

from django.db                                          import models

from PyProject_ShiftIT.autenticacao.models              import Usuario

       
        
#---------------------------DOCUMENTO -----------------------------------    
    
class Documento(models.Model):
    id_documento        = models.IntegerField(max_length=3, primary_key=True, null= False, blank=True)
    usuario             = models.ForeignKey(Usuario, null= False, verbose_name='Usuário')
    assunto             = models.CharField(max_length=200, verbose_name='Assunto') 
    arquivo             = models.FileField(upload_to='/multimidia/', max_length=100)
    
    class Meta:
        db_table= 'tb_documento'
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'
    
    def __unicode__(self):
        return self.id_documento
    
    def save(self):  
        if self.id_documento == '' or self.id_documento== None:
            if len(Documento.objects.order_by('-id_documento')) > 0:   
                iUltimoRegistro = Documento.objects.order_by('-id_documento')[0] 
                self.id_documento= iUltimoRegistro.pk + 1
            else:
                self.id_documento= 1
        super(Documento, self).save()
        
#---------------------------TIPO PRIORIDADE -----------------------------------   
        
class Tipo_Prioridade(models.Model):
    id_tipo_prioridade  = models.IntegerField(max_length=3, primary_key=True, null= False, blank=True)
    descricao           = models.CharField(max_length=200) 
            
    class Meta:
        db_table= 'tb_tipo_prioridade'
        verbose_name = 'Tipo de Prioridade'
        verbose_name_plural = 'Tipos de Prioridade'
    
    def __unicode__(self):
        return self.descricao
    
    def save(self):  
        if self.id_tipo_prioridade == '' or self.id_tipo_prioridade== None:
            if len(Tipo_Prioridade.objects.order_by('-id_tipo_prioridade')) > 0:   
                iUltimoRegistro = Tipo_Prioridade.objects.order_by('-id_tipo_prioridade')[0] 
                self.id_tipo_prioridade= iUltimoRegistro.pk + 1
            else:
                self.id_tipo_prioridade= 1
        super(Tipo_Prioridade, self).save()
        
#---------------------------TIPO ESTADO -----------------------------------   
        
class Tipo_Estado(models.Model):
    id_tipo_estado      = models.IntegerField(max_length=3, primary_key=True, null= False, blank=True)
    descricao           = models.CharField(max_length=200) 
            
    class Meta:
        db_table= 'tb_tipo_estado'
        verbose_name = 'Tipo de Estado'
        verbose_name_plural = 'Tipos de Estado'
    
    def __unicode__(self):
        return self.descricao
    
    def save(self):  
        if self.id_tipo_estado == '' or self.id_tipo_estado== None:
            if len(Tipo_Estado.objects.order_by('-id_tipo_estado')) > 0:   
                iUltimoRegistro = Tipo_Estado.objects.order_by('-id_tipo_estado')[0] 
                self.id_tipo_estado= iUltimoRegistro.pk + 1
            else:
                self.id_tipo_estado= 1
        super(Tipo_Estado, self).save()
        
#---------------------------BUG -----------------------------------    
    
class Bug(models.Model):
    id_bug              = models.IntegerField(max_length=3, primary_key=True, null= False, blank=True)
    usuario             = models.ForeignKey(Usuario, null= False, verbose_name='Usuário')
    tipo_prioridade     = models.ForeignKey(Tipo_Prioridade, null= False, verbose_name='Tipo de Prioridade')
    descricao           = models.CharField(max_length=500, verbose_name='Descrição') 
    nome_contato        = models.CharField(max_length=200, verbose_name='Nome de Contato')
    email_contato       = models.CharField(max_length=200, verbose_name='Email')
    telefone_contato    = models.CharField(max_length=100, verbose_name='Telefone')
    imagem              = models.FileField(upload_to='/multimidia/', max_length=100)
    data                = models.DateTimeField(null= True, verbose_name='Data')
    
    class Meta:
        db_table= 'tb_bug'
        verbose_name = 'Bug'
        verbose_name_plural = 'Bugs'
    
    def __unicode__(self):
        return self.descricao
    
    def save(self):  
        if self.id_bug == '' or self.id_bug== None:
            if len(Bug.objects.order_by('-id_bug')) > 0:   
                iUltimoRegistro = Bug.objects.order_by('-id_bug')[0] 
                self.id_bug= iUltimoRegistro.pk + 1
            else:
                self.id_bug= 1
        super(Bug, self).save()

#---------------------------ESTADO BUG -----------------------------------   
        
class Estado_Bug(models.Model):
    id_estado_bug       = models.IntegerField(max_length=3, primary_key=True, null= False, blank=True)
    bug                 = models.ForeignKey(Bug, null= False, verbose_name='Bug')
    tipo_estado         = models.ForeignKey(Tipo_Estado, null= False, verbose_name='Tipo de Estado')
    comentario          = models.CharField(max_length=500) 
    data                = models.DateTimeField(null= True, verbose_name='Data')
            
    class Meta:
        db_table= 'tb_estado_bug'
        verbose_name = 'Estado de Bug'
        verbose_name_plural = 'Estado de Bug'
    
    def __unicode__(self):
        return self.comentario
    
    def save(self):  
        if self.id_estado_bug == '' or self.id_estado_bug== None:
            if len(Estado_Bug.objects.order_by('-id_estado_bug')) > 0:   
                iUltimoRegistro = Estado_Bug.objects.order_by('-id_estado_bug')[0] 
                self.id_estado_bug= iUltimoRegistro.pk + 1
            else:
                self.id_estado_bug= 1
        super(Estado_Bug, self).save()
        
        
#-----------------------------PERGUNTA BUG---------------------------------------
        
class Pergunta_Bug(models.Model):
    id_pergunta_Bug     = models.IntegerField(max_length=3, primary_key=True, null= False, blank=True)
    pergunta            = models.CharField(max_length=500, verbose_name='Pergunta') 
        
    class Meta:
        db_table= 'tb_pergunta_bug'
        verbose_name = 'Pergunta de Bug'
        verbose_name_plural = 'Perguntas de Bug'
    
    def __unicode__(self):
        return str(self.id_pergunta_bug)
    
    def save(self):  
        if self.id_pergunta_Bug == '' or self.id_pergunta_Bug== None:
            if len(Pergunta_Bug.objects.order_by('-id_pergunta_Bug')) > 0:   
                iUltimoRegistro = Pergunta_Bug.objects.order_by('-id_pergunta_Bug')[0] 
                self.id_pergunta_Bug= iUltimoRegistro.pk + 1
            else:
                self.id_pergunta_Bug= 1
        super(Pergunta_Bug, self).save()
        
#-----------------------------RESPOSTA CONTATO---------------------------------------
        
class Resposta_Bug(models.Model):
    id_resposta_bug     = models.IntegerField(max_length=3, primary_key=True, null= False, blank=True)
    pergunta            = models.ForeignKey(Pergunta_Bug, null= False, verbose_name='Pergunta')
    bug                 = models.ForeignKey(Bug, null= False, verbose_name='Bug')
    resposta            = models.CharField(max_length=500, verbose_name='Resposta') 
        
    class Meta:
        db_table= 'tb_resposta_bug'
        verbose_name = 'Resposta de Bug'
        verbose_name_plural = 'Respostas de Bug'
    
    def __unicode__(self):
        return str(self.id_resposta_bug)
    
    def save(self):  
        if self.id_resposta_bug == '' or self.id_resposta_bug== None:
            if len(Resposta_Bug.objects.order_by('-id_resposta_bug')) > 0:   
                iUltimoRegistro = Resposta_Bug.objects.order_by('-id_resposta_bug')[0] 
                self.id_resposta_bug= iUltimoRegistro.pk + 1
            else:
                self.id_resposta_bug= 1
        super(Resposta_Bug, self).save()

