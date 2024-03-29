'''
Created on Jul 18, 2012

@author: Shift IT | www.shiftit.com.br
'''

from django.core                                    import mail
from django.conf                                    import settings

import logging

class Controle(object):
    
    oLogger= logging.getLogger('PyProject_Startuplay.controle')
    
    def setLogger(self, vLogger):
        self.oLogger= vLogger
    
    def getLogger(self):
        return self.oLogger
    
    def enviarEmail(self, vTitulo, vTexto, vEmailDestino, vEmailRemetente):
        try:                
            if settings.EMAIL:
                mail.send_mail(
                    subject=vTitulo,
                    message=vTexto,
                    from_email=vEmailRemetente,
                    recipient_list=[vEmailDestino],
                    )
            return True
        except Exception, e:
            self.getLogger().error('Nao foi possivel enviar email: ' + str(e))
            return False