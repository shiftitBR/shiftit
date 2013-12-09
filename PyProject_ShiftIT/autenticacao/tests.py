# -*- coding: utf-8 -*-
from django.test                                import TestCase

from autenticacao.models                        import Usuario

class Test(TestCase):
    
    def setUp(self):
        self.mokarUsuario()
        pass
    
    def tearDown(self):
        Usuario.objects.all().delete()
        pass

    def testsObtemUsuario(self):
        iUsuario = Usuario().obtemUsuario(1)
        self.assertEquals(1, iUsuario.id)
        
    def testspossuiUsuario(self):
        iPossuiUsuario = Usuario().possuiUsuario(1)
        self.assertEquals(True, iPossuiUsuario)
 
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
    
