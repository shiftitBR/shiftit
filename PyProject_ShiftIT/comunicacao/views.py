# -*- coding: utf-8 -*-
from django.shortcuts                           import render_to_response
from django.template                            import RequestContext
from django.http                                import HttpResponseRedirect

from PyProject_ShiftIT.comunicacao.forms     import FormContato
from PyProject_ShiftIT.comunicacao.controle  import Controle as ComunicacaoControle

import datetime

def contato (vRequest, vTitulo):
    
    if vRequest.method == 'POST':
        form = FormContato(vRequest.POST)

        if form.is_valid() :
            iContato              = form.save(commit=False)
            iContato.data         = str(datetime.datetime.today())[:19]
            iContato.save()
            
            ComunicacaoControle().enviarEmail('[Titulo]', iContato.mensagem, 'diego.costa@shiftit.com.br', 'diego.costa@shiftit.com.br') 
            return HttpResponseRedirect('/')
    else:
        form= FormContato()
        
    return render_to_response(
        'contato/contato.html',
        locals(),
        context_instance=RequestContext(vRequest),
        )
    

