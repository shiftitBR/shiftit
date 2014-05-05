# -*- coding: utf-8 -*-
from django.shortcuts                       import render_to_response
from django.template                        import RequestContext
from django.contrib                         import messages
from django.http                            import HttpResponseRedirect

from autenticacao.models                    import Usuario
from comunicacao.forms                      import FormEmail
from comunicacao.controle                   import Controle as ComunicacaoControle

import datetime

def home(vRequest, vTitulo):
    iUsuario            = Usuario().obtemUsuario(vRequest.user.id)
    iHome               = True

    if vRequest.method == 'POST':
        form = FormEmail(vRequest.POST)
        if form.is_valid() :
            iEmail              = form.save(commit=False)
            iEmail.data         = str(datetime.datetime.today())[:19]
            iEmail.save()
            
            if 'gmail' in iEmail.email:
                iRemetente  = 'contato@shiftit.com.br'
            else:
                iRemetente  = iEmail.email
            
            ComunicacaoControle().enviarEmail('[Contato Shift it]', iEmail.mensagem, 'contato@shiftit.com.br', iRemetente) 
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
    
def servicos(vRequest, vTitulo):
    iUsuario           = Usuario().obtemUsuario(vRequest.user.id)
    
    if vRequest.method == 'POST':
        form = FormEmail(vRequest.POST)

        if form.is_valid() :
            iEmail                  = form.save(commit=False)
            iEmail.data             = str(datetime.datetime.today())[:19]
            iEmail.save()
            
            if 'gmail' in iEmail.email:
                iRemetente  = 'contato@shiftit.com.br'
            else:
                iRemetente  = iEmail.email
            
            ComunicacaoControle().enviarEmail('[Serviço Shift it]', iEmail.mensagem, 'contato@shiftit.com.br', iRemetente) 
            return HttpResponseRedirect('/servicos/')
    else:
        form= FormEmail()
    
    return render_to_response(
        'o_que_fazemos/servicos.html',
        locals(),
        context_instance=RequestContext(vRequest),
        )
    
def google(vRequest, vTitulo):
        
    return render_to_response(
        'google/google6196345173a7df0a.html',
        locals(),
        context_instance=RequestContext(vRequest),
        )