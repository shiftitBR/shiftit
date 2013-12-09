# -*- coding: utf-8 -*-
'''
Created on Jul 11, 2012

@author: Shift IT | www.shiftit.com.br
'''

from django.db                                          import models

from autenticacao.models                                import Usuario
from bugtracker.objetos_auxiliares                      import Bug as BugAux

import logging
import datetime

#---------------------------DOCUMENTO -----------------------------------    
    
class Documento(models.Model):
    usuario             = models.ForeignKey(Usuario, null= False, blank=True, verbose_name='Usuário')
    assunto             = models.CharField(max_length=200, blank=True, verbose_name='Assunto') 
    arquivo             = models.FileField(upload_to='multimidia/fotos/', max_length=100)
    
    class Meta:
        db_table= 'tb_documento'
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'
    
    def __unicode__(self):
        return self.id
        
#---------------------------TIPO PRIORIDADE -----------------------------------   
        
class Tipo_Prioridade(models.Model):
    descricao           = models.CharField(max_length=200, blank=True) 
            
    class Meta:
        db_table= 'tb_tipo_prioridade'
        verbose_name = 'Tipo de Prioridade'
        verbose_name_plural = 'Tipos de Prioridade'
    
    def __unicode__(self):
        return self.descricao
    
    def obtemListaTipoPrioridade(self,):
        try:
            iLista= Tipo_Prioridade.objects.all()
            return iLista
        except Exception, e:
            logging.getLogger('PyProject_ShiftIT.controle').error('Nao foi possivel obtem Lista Tipo Prioridade: ' + str(e))
            return None  
        
    def obtemTipoPrioridade(self, iIDTipoPrioridade):
        try:
            iTipoPrioridade= Tipo_Prioridade.objects.filter(id = iIDTipoPrioridade)[0]
            return iTipoPrioridade
        except Exception, e:
            logging.getLogger('PyProject_ShiftIT.controle').error('Nao foi possivel obtem Tipo Prioridade: ' + str(e))
            return None  
        
#---------------------------TIPO ESTADO -----------------------------------   
        
class Tipo_Estado(models.Model):
    descricao           = models.CharField(max_length=200) 
            
    class Meta:
        db_table= 'tb_tipo_estado'
        verbose_name = 'Tipo de Estado'
        verbose_name_plural = 'Tipos de Estado'
    
    def __unicode__(self):
        return '(%s - %s)' % (str(self.id), self.descricao)
        
#---------------------------BUG -----------------------------------    
    
class Bug(models.Model):
    usuario             = models.ForeignKey(Usuario, null= False, blank=True, verbose_name='Usuário')
    tipo_prioridade     = models.ForeignKey(Tipo_Prioridade, null= False, blank=True, verbose_name='Tipo Prioridade')
    descricao           = models.TextField(max_length=500, blank=True, verbose_name='Descrição') 
    nome_contato        = models.CharField(max_length=200, blank=True, verbose_name='Nome de Contato')
    email_contato       = models.CharField(max_length=200, blank=True, verbose_name='Email')
    telefone_contato    = models.CharField(max_length=100, blank=True, verbose_name='Telefone')
    imagem              = models.FileField(upload_to='multimidia/fotos/', blank=True, max_length=100)
    data                = models.DateTimeField(null= True, blank=True, verbose_name='Data')
    
    class Meta:
        db_table= 'tb_bug'
        verbose_name = 'Bug'
        verbose_name_plural = 'Bugs'
    
    def __unicode__(self):
        return self.descricao
        
    def criaBug(self, vIDUsuario, vIDTipoPrioridade, vDescricao, vNomeContato, vEmailContato, vTelefoneContato, vImagem):
        try:
            iBug                        = Bug()
            iBug.usuario                = Usuario.objects.filter(id= vIDUsuario)[0]
            iBug.tipo_prioridade        = Tipo_Prioridade.objects.filter(id= vIDTipoPrioridade)[0]
            iBug.descricao              = vDescricao
            iBug.nome_contato           = vNomeContato
            iBug.email_contato          = vEmailContato
            iBug.telefone_contato       = vTelefoneContato
            iBug.imagem                 = vImagem
            iBug.data                   = datetime.datetime.now()
            iBug.save()
        except Exception, e:
            logging.getLogger('PyProject_ShiftIT.controle').error('Nao foi possivel criar bug: ' + str(e))
            return False
    
    def alteraEstado(self, vBug, vIDTipoEstado, vComentario):
        try:
            iEstadoBug              = Estado_Bug()
            iEstadoBug.bug          = vBug 
            iEstadoBug.tipo_estado  = Tipo_Estado.objects.filter(id= vIDTipoEstado)[0]
            iEstadoBug.comentario   = vComentario
            iEstadoBug.data         = datetime.datetime.now()
            iEstadoBug.save()
        except Exception, e:
            logging.getLogger('PyProject_ShiftIT.controle').error('Nao foi possivel alterar estado: ' + str(e))
            return False
    
    def obtemEstadoAtual(self, vIDBug):
        try:
            iEstadoAtual= Estado_Bug.objects.filter(bug__id= vIDBug).order_by('-data')[0]
            return iEstadoAtual
        except Exception, e:
            logging.getLogger('PyProject_ShiftIT.controle').error('Nao foi possivel obter o estado atual do bug: ' + str(e))
            return False
        
#---------------------------ESTADO BUG -----------------------------------   
        
class Estado_Bug(models.Model):
    bug                 = models.ForeignKey(Bug, null= False, verbose_name='Bug')
    tipo_estado         = models.ForeignKey(Tipo_Estado, null= False, verbose_name='Tipo Estado')
    comentario          = models.TextField(max_length=500) 
    data                = models.DateTimeField(null= True, verbose_name='Data')
            
    class Meta:
        db_table= 'tb_estado_bug'
        verbose_name = 'Estado de Bug'
        verbose_name_plural = 'Estado de Bug'
    
    def __unicode__(self):
        return self.comentario
        
    def obtemListaBugsAux(self, vUsuario):
        try:
            iListaBug   = Bug.objects.filter(usuario= vUsuario).order_by('-id')
            iListaAux   = []
            for bug in iListaBug:
                iBug                = BugAux()
                iBug.bug            = bug
                iBug.estados        = Estado_Bug.objects.filter(bug= bug)
                iBug.possuiestado   = (len(iBug.estados) > 0)
                iListaAux.append(iBug)
            return iListaAux
        except Exception, e:
            logging.getLogger('PyProject_ShiftIT.controle').error('Nao foi possivel obtem Lista Bugs Aux: ' + str(e))
            return False

#-----------------------------PERGUNTA BUG---------------------------------------
        
class Pergunta_Bug(models.Model):
    pergunta            = models.TextField(max_length=500, verbose_name='Pergunta') 
        
    class Meta:
        db_table= 'tb_pergunta_bug'
        verbose_name = 'Pergunta de Bug'
        verbose_name_plural = 'Perguntas de Bug'
    
    def __unicode__(self):
        return self.pergunta
        
    def obtemPerguntaBug(self, vIDPerguntaBug):
        try:
            iPerguntaBug= Pergunta_Bug.objects.filter(id= vIDPerguntaBug)[0]
            return iPerguntaBug
        except Exception, e:
            logging.getLogger('PyProject_ShiftIT.controle').error('Nao foi possivel obtem Pergunta Bug: ' + str(e))
            return None   
        
#-----------------------------RESPOSTA CONTATO---------------------------------------
        
class Resposta_Bug(models.Model):
    pergunta            = models.ForeignKey(Pergunta_Bug, null= False, verbose_name='Pergunta')
    bug                 = models.ForeignKey(Bug, null= False, verbose_name='Bug')
    resposta            = models.TextField(max_length=500, verbose_name='Resposta') 
        
    class Meta:
        db_table= 'tb_resposta_bug'
        verbose_name = 'Resposta de Bug'
        verbose_name_plural = 'Respostas de Bug'
    
    def __unicode__(self):
        return self.resposta
