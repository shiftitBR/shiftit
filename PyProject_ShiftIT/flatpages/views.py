# -*- coding: utf-8 -*-
from django.shortcuts                       import render_to_response
from django.template                        import RequestContext

from PyProject_ShiftIT.autenticacao.models  import Usuario
from PyProject_ShiftIT.comunicacao.forms    import FormEmail
from django.contrib                         import messages
from django.http                            import HttpResponseRedirect
from PyProject_ShiftIT.comunicacao.controle import Controle as ComunicacaoControle

import datetime

def home(vRequest, vTitulo):
    iUsuario           = Usuario().obtemUsuario(vRequest.user.id)
    
    if vRequest.method == 'POST':
        form = FormEmail(vRequest.POST)

        if form.is_valid() :
            iEmail              = form.save(commit=False)
            iEmail.data         = str(datetime.datetime.today())[:19]
            iEmail.save()
            
            ComunicacaoControle().enviarEmail('[Contato Shift it]', iEmail.mensagem, 'diego.costa@shiftit.com.br', 'diego.costa@shiftit.com.br') 
            messages.info(vRequest, 'Sua mensagem foi enviada com sucesso!')
            return HttpResponseRedirect('/')
        else:
            messages.info(vRequest, 'O campo E-mail é obrigatório!')
    else:
        form= FormEmail()
    
    return render_to_response(
        'home/home.html',
        locals(),
        context_instance=RequestContext(vRequest),
        )


def time(vRequest, vTitulo):
    iUsuario           = Usuario().obtemUsuario(vRequest.user.id)
    
    return render_to_response(
        'time/time.html',
        locals(),
        context_instance=RequestContext(vRequest),
        )
    
def como_fazemos(vRequest, vTitulo):
    iUsuario           = Usuario().obtemUsuario(vRequest.user.id)
    
    return render_to_response(
        'como_fazemos/como_fazemos.html',
        locals(),
        context_instance=RequestContext(vRequest),
        )
    
def o_que_fazemos(vRequest, vTitulo):
    iUsuario           = Usuario().obtemUsuario(vRequest.user.id)
    
    return render_to_response(
        'o_que_fazemos/o_que_fazemos.html',
        locals(),
        context_instance=RequestContext(vRequest),
        )