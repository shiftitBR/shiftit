# -*- coding: utf-8 -*-
from django.shortcuts                       import render_to_response
from django.template                        import RequestContext



def adicionar_bug(vRequest, vTitulo):
    

    return render_to_response(
        'bug/adicionar_bug.html',
        locals(),
        context_instance=RequestContext(vRequest),
        )
    
def documentos(vRequest, vTitulo):
    

    return render_to_response(
        'documentos/documentos.html',
        locals(),
        context_instance=RequestContext(vRequest),
        )
    
def painel_controle(vRequest, vTitulo):
    

    return render_to_response(
        'painel_controle/painel_controle.html',
        locals(),
        context_instance=RequestContext(vRequest),
        )