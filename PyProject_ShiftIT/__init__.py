from django.conf import settings
from django.contrib.auth.models import User

import controle

oControle= controle.Controle()

if not oControle.inicializaAplicacao():
    print 'Problemas ao inicilizar a aplicacao!'

