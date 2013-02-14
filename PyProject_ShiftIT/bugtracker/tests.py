# -*- coding: utf-8 -*-
from django.test                                import TestCase
from django.conf                                import settings

from PyProject_ShiftIT.autenticacao.models      import Usuario
from PyProject_ShiftIT.bugtracker.models        import Documento, Tipo_Prioridade, Tipo_Estado, Bug,\
    Estado_Bug, Pergunta_Bug, Resposta_Bug
    
import datetime

class Test(TestCase):
    
    def setUp(self):
        self.mokarUsuario()
        self.mokarDocumento()
        self.mokarTipoPrioridade()
        self.mokarBug()
        self.mokarEstadoBug()
        self.mokarPerguntaBug()
        self.mokarRespostaBug()
        pass
    
    
    def tearDown(self):
        Usuario.objects.all().delete()
        Documento.objects.all().delete()
        Tipo_Prioridade.objects.all().delete()
        Bug.objects.all().delete()
        Estado_Bug.objects.all().delete()
        Pergunta_Bug.objects.all().delete()
        Resposta_Bug.objects.all().delete()
        pass
    
    #-----------------------------------------------------MOKS---------------------------------------------------
    
    def mokarUsuario(self):
        iUsuario                    = Usuario()
        iUsuario.cnpj               = 'teste'
        iUsuario.razao_social       = 'teste'
        iUsuario.nome_fantasia      = 'teste'
        iUsuario.endereco           = 'teste'
        iUsuario.cidade             = 'teste'
        iUsuario.uf                 = 'teste'
        iUsuario.nome_responsavel   = 'teste'
        iUsuario.telefone           = 'teste'
        iUsuario.save()
    
    def mokarDocumento(self):
        iDocumento                  = Documento()
        iDocumento.usuario          = Usuario.objects.all()[0]
        iDocumento.assunto          = 'diego.costa@shiftit.com.br'
        iDocumento.arquivo          = '%s/media/testes/teste.pdf' % settings.MEDIA_ROOT
        iDocumento.save()
        
    def mokarTipoPrioridade(self):
        iTipoPrioridade             = Tipo_Prioridade()
        iTipoPrioridade.descricao   = 'teste'
        iTipoPrioridade.save()
        
    def mokarTipoEstado(self):
        iTipoEstado                 = Tipo_Estado()
        iTipoEstado.descricao       = 'teste'
        iTipoEstado.save()
    
    def mokarBug(self):
        iBug                        = Bug()
        iBug.usuario                = Usuario.objects.all()[0]
        iBug.tipo_prioridade        = Tipo_Prioridade.objects.all()[0]
        iBug.descricao              = 'teste'
        iBug.nome_Contato           = 'teste'
        iBug.email_Contato          = 'teste'
        iBug.telefone_Contato       = 'teste'
        iBug.imagem                 = '%s/media/testes/teste.pdf' % settings.MEDIA_ROOT
        iBug.data                   = datetime.datetime.now()
        iBug.save()
        
    def mokarEstadoBug(self):
        iEstadoBug                  = Estado_Bug()
        iEstadoBug.bug              = Bug.objects.all()[0]  
        iEstadoBug.tipo_estado      = Tipo_Estado.objects.all()[0]
        iEstadoBug.comentario       = 'teste'
        iEstadoBug.data             = datetime.datetime.now()
        iEstadoBug.save()
        
    def mokarPerguntaBug(self):
        iPerguntaBug              = Pergunta_Bug()
        iPerguntaBug.pergunta     = 'Qual seu nome?'
        iPerguntaBug.save()
        
    def mokarRespostaBug(self):
        iRespostaBug              = Resposta_Bug()
        iRespostaBug.pergunta     = Pergunta_Bug.objects.all()[0]
        iRespostaBug.Bug          = Bug.objects.all()[0]
        iRespostaBug.resposta     = 'Meu nome não é Johny'
        iRespostaBug.save()
