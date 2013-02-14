# -*- coding: utf-8 -*-
from django.shortcuts                       import render_to_response
from django.template                        import RequestContext

from PyProject_ShiftIT.autenticacao.models  import Usuario


def home(vRequest, vTitulo):
    iUsuario           = Usuario().obtemUsuario(vRequest.user.id)
    
    return render_to_response(
        'home/home.html',
        locals(),
        context_instance=RequestContext(vRequest),
        )
