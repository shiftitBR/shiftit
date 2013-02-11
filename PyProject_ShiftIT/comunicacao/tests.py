# -*- coding: utf-8 -*-
from django.test                                import TestCase
from PyProject_Startuplay.comunicacao.models    import Email
    
import datetime

class Test(TestCase):
    
    def setUp(self):
        self.mokarEmail()
        pass
    
    
    def tearDown(self):
        Email.objects.all().delete()
        pass
    
    #-----------------------------------------------------MOKS---------------------------------------------------

    def mokarEmail(self):
        iEmail                      = Email()
        iEmail.nome                 = 'Diego Costa'
        iEmail.email                = 'diego.costa@shiftit.com.br'
        iEmail.telefone             = '(48) 3333-33-33'
        iEmail.mensagem             = 'Mensagem de teste'
        iEmail.data                 = datetime.datetime.now()
        iEmail.save()
