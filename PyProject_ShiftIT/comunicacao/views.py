# -*- coding: utf-8 -*-
from django.shortcuts                           import render_to_response
from django.template                            import RequestContext
from django.http                                import HttpResponseRedirect

from PyProject_ShiftIT.comunicacao.forms        import FormEmail
from PyProject_ShiftIT.comunicacao.controle     import Controle as ComunicacaoControle

import datetime

def contato (vRequest, vTitulo):
    
    if vRequest.method == 'POST':
        form = FormEmail(vRequest.POST)

        if form.is_valid() :
            iEmail                  = form.save(commit=False)
            iEmail.data             = str(datetime.datetime.today())[:19]
            iEmail.save()
            
            ComunicacaoControle().enviarEmail('[Titulo]', iEmail.mensagem, 'diego.costa@shiftit.com.br', 'diego.costa@shiftit.com.br') 
            return HttpResponseRedirect('/')
    else:
        form= FormEmail()
        
    return render_to_response(
        'contato/contato.html',
        locals(),
        context_instance=RequestContext(vRequest),
        )
    
def briefing (vRequest, vTitulo):
    
    if vRequest.method == 'POST':
        print '>>>>>>>>>>>>'
    return render_to_response(
        'briefing/briefing.html',
        locals(),
        context_instance=RequestContext(vRequest),
        )
