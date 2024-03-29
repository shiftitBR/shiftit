# -*- coding: utf-8 -*-
from django.test                                import TestCase

from comunicacao.models                         import Email
from comunicacao.models                         import Contato
from comunicacao.models                         import Pergunta_Contato
from comunicacao.models                         import Resposta_Contato
    
import datetime

class Test(TestCase):
    
    def setUp(self):
        self.mokarEmail()
        self.mokarContato()
        self.mokarPerguntaContato()
        self.mokarRespostaContato()
        pass
    
    
    def tearDown(self):
        Email.objects.all().delete()
        Contato.objects.all().delete()
        Pergunta_Contato.objects.all().delete()
        Resposta_Contato.objects.all().delete()
        pass

    def testsobtemPerguntaContato(self):
        iPerguntaContato= Pergunta_Contato().obtemPerguntaContato(1)
        self.assertEquals(1, iPerguntaContato.id)
    
    #-----------------------------------------------------MOKS---------------------------------------------------

    def mokarEmail(self):
        iEmail                      = Email()
        iEmail.nome                 = 'Diego Costa'
        iEmail.email                = 'diego.costa@shiftit.com.br'
        iEmail.telefone             = '(48) 3333-33-33'
        iEmail.mensagem             = 'Mensagem de teste'
        iEmail.data                 = datetime.datetime.now()
        iEmail.save()
        
    def mokarContato(self):
        iContato                      = Contato()
        iContato.nome                 = 'Diego Costa'
        iContato.email                = 'diego.costa@shiftit.com.br'
        iContato.telefone             = '(48) 3333-33-33'
        iContato.data                 = datetime.datetime.now()
        iContato.save()
        
    def mokarPerguntaContato(self):
        iPerguntaContato              = Pergunta_Contato()
        iPerguntaContato.pergunta     = 'Qual seu nome?'
        iPerguntaContato.save()
        
    def mokarRespostaContato(self):
        iRespostaContato              = Resposta_Contato()
        iRespostaContato.pergunta     = Pergunta_Contato.objects.all()[0]
        iRespostaContato.contato      = Contato.objects.all()[0]
        iRespostaContato.resposta     = 'Meu nome não é Johny'
        iRespostaContato.save()
