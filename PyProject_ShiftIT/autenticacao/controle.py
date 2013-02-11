# -*- coding: utf-8 -*-
'''
Created on Jul 18, 2012

@author: Shift IT | www.shiftit.com.br
'''

from django.conf                                    import settings

import logging
import urllib

class Controle(object):
    
    oLogger= logging.getLogger('PyProject_ShiftIT.controle')
    
    def setLogger(self, vLogger):
        self.oLogger= vLogger
    
    def getLogger(self):
        return self.oLogger
    
    def download_photo(self, img_url, filename):
        try:  
            file_path = "%s%s" % (settings.MEDIA_ROOT + '/multimidia/avatar/', filename)
            downloaded_image = file(file_path, "wb")
            image_on_web = urllib.urlopen(img_url)
            while True:
                buf = image_on_web.read(65536)
                if len(buf) == 0:
                    break
                downloaded_image.write(buf)
            downloaded_image.close()
            image_on_web.close()
        
            return file_path
        except Exception, e:
            self.getLogger().error('Nao foi possivel download photo: ' + str(e))
            return False
        