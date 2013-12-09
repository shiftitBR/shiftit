# -*- coding: utf-8 -*-
from django.test                                import TestCase
from django.conf                                import settings

from autenticacao.models                        import Usuario
from bugtracker.models                          import Documento, Tipo_Prioridade, Tipo_Estado, Bug,\
    Estado_Bug, Pergunta_Bug, Resposta_Bug
    
import datetime
import constantes

class Test(TestCase):
    
    def setUp(self):
        self.mokarUsuario()
        self.mokarDocumento()
        self.mokarTipoPrioridade()
        self.mokarBug()
        self.mokarTipoEstado()
        self.mokarEstadoBug()
        self.mokarAlteraEstadoBug()
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
    
    #-----------------------------------------------------TESTES---------------------------------------------------
    
    def testCriarBug_Simples(self):
        iBug                        = Bug()
        iBug.usuario                = Usuario.objects.all()[0]
        iBug.tipo_prioridade        = Tipo_Prioridade.objects.all()[0]
        iBug.descricao              = 'descricao_teste'
        iBug.nome_contato           = 'nome_teste'
        iBug.email_contato          = 'emai_teste'
        iBug.telefone_contato       = 'telefone_teste'
        iBug.imagem                 = '%s/media/testes/teste.pdf' % settings.MEDIA_ROOT
        iBug.data                   = datetime.datetime.now()
        iBug.save()
        self.assertEquals(Bug.objects.count(), 3)
    
    def testCriarBug_Metodo(self):
        iBug                        = Bug()
        iUsuario                    = Usuario.objects.all()[0].id
        iTipoPrioridade             = Tipo_Prioridade.objects.all()[0].id
        iDescricao                  = 'descricao_teste'
        iNomeContato                = 'nome_teste'
        iEmailContato               = 'emai_teste'
        iTelefoneContato            = 'telefone_teste'
        iImagem                     = '%s/media/testes/teste.pdf' % settings.MEDIA_ROOT
        iBug.criaBug(iUsuario, iTipoPrioridade, iDescricao, iNomeContato, iEmailContato, iTelefoneContato, iImagem)
        self.assertEquals(Bug.objects.count(), 3)
        
    
    def testAlteraEstadoBug(self):
        iBug        = Bug.objects.filter(id= 2)[0]
        iComentario = 'Comentario teste'
        iBug.alteraEstado(iBug, constantes.cntEstadoBug_EmAnalise, iComentario)
        self.assertEquals(Estado_Bug.objects.filter(bug__id= 2)[0].tipo_estado.id, constantes.cntEstadoBug_EmAnalise)
    
    def testObtemEstadoAtualDoBug(self):
        iBug        = Bug.objects.filter(id= 1)[0]
        iEstadoAtual= iBug.obtemEstadoAtual(iBug.id)
        self.assertEquals(iEstadoAtual.tipo_estado.id, constantes.cntEstadoBug_EmAnalise)
        
#----------------------------------------------MOKS-------------------------------------
    
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
        iTipoEstado.id              = constantes.cntEstadoBug_Novo
        iTipoEstado.descricao       = 'novo'
        iTipoEstado.save()
        
        iTipoEstado.id              = constantes.cntEstadoBug_EmAnalise
        iTipoEstado.descricao       = 'em analise'
        iTipoEstado.save()
        
        iTipoEstado.id              = constantes.cntEstadoBug_EmEspera
        iTipoEstado.descricao       = 'em espera'
        iTipoEstado.save()
        
        iTipoEstado.id              = constantes.cntEstadoBug_EmDesenvolvimento
        iTipoEstado.descricao       = 'em desenvolvimento'
        iTipoEstado.save()
        
        iTipoEstado.id              = constantes.cntEstadoBug_AguardandoAprovacao
        iTipoEstado.descricao       = 'aguardando aprovacao'
        iTipoEstado.save()
        
        iTipoEstado.id              = constantes.cntEstadoBug_Finalizado
        iTipoEstado.descricao       = 'finalizado'
        iTipoEstado.save()
        
        iTipoEstado.id              = constantes.cntEstadoBug_EmProducao
        iTipoEstado.descricao       = 'em producao'
        iTipoEstado.save()
    
    def mokarBug(self):
        iBug                        = Bug()
        iBug.usuario                = Usuario.objects.all()[0]
        iBug.tipo_prioridade        = Tipo_Prioridade.objects.all()[0]
        iBug.descricao              = 'teste1'
        iBug.nome_Contato           = 'teste1'
        iBug.email_Contato          = 'teste1'
        iBug.telefone_Contato       = 'teste1'
        iBug.imagem                 = '%s/media/testes/teste.pdf' % settings.MEDIA_ROOT
        iBug.data                   = datetime.datetime.now()
        iBug.save()
        
        iBug                        = Bug()
        iBug.usuario                = Usuario.objects.all()[0]
        iBug.tipo_prioridade        = Tipo_Prioridade.objects.all()[0]
        iBug.descricao              = 'teste2'
        iBug.nome_Contato           = 'teste2'
        iBug.email_Contato          = 'teste2'
        iBug.telefone_Contato       = 'teste2'
        iBug.imagem                 = '%s/media/testes/teste.pdf' % settings.MEDIA_ROOT
        iBug.data                   = datetime.datetime.now()
        iBug.save()
        
    def mokarEstadoBug(self):
        iEstadoBug                  = Estado_Bug()
        iEstadoBug.bug              = Bug.objects.all()[0]  
        iEstadoBug.tipo_estado      = Tipo_Estado.objects.all()[0]
        iEstadoBug.comentario       = 'teste - novo'
        iEstadoBug.data             = datetime.datetime.now()
        iEstadoBug.save()
    
    def mokarAlteraEstadoBug(self):
        iBug        = Bug.objects.filter(id= 1)[0]
        iComentario = 'Comentario teste'
        iBug.alteraEstado(iBug, constantes.cntEstadoBug_EmAnalise, iComentario)
        
    def mokarPerguntaBug(self):
        iPerguntaBug              = Pergunta_Bug()
        iPerguntaBug.pergunta     = 'Qual seu nome?'
        iPerguntaBug.save()
        
    def mokarRespostaBug(self):
        iRespostaBug              = Resposta_Bug()
        iRespostaBug.pergunta     = Pergunta_Bug.objects.all()[0]
        iRespostaBug.bug          = Bug.objects.all()[0]
        iRespostaBug.resposta     = 'Meu nome não é Johny'
        iRespostaBug.save()
