# -*- coding: utf-8 -*-
from django.shortcuts                           import render_to_response
from django.template                            import RequestContext
from django.http                                import HttpResponseRedirect
from django.contrib                             import messages

from PyProject_ShiftIT.comunicacao.forms        import FormEmail, FormContato
from PyProject_ShiftIT.comunicacao.controle     import Controle as ComunicacaoControle
from PyProject_ShiftIT.comunicacao.models       import Pergunta_Contato, Resposta_Contato

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
    
    iListaPerguntas = Pergunta_Contato.objects.all()
    
    if vRequest.method == 'POST':
        form = FormContato(vRequest.POST)
        
        if form.is_valid() :
            iContato                = form.save(commit=False)
            iContato.data           = str(datetime.datetime.today())[:19]
            iContato.save()
            for pergunta in iListaPerguntas:
                if 'resposta_' + str(pergunta.id_pergunta_contato) in vRequest.POST:
                    iResposta           = Resposta_Contato()
                    iResposta.pergunta  = Pergunta_Contato().obtemPerguntaContato(pergunta.id_pergunta_contato)
                    iResposta.contato   = iContato
                    iResposta.resposta  = vRequest.POST.get('resposta_' + str(pergunta.id_pergunta_contato))
                    iResposta.save()
            return HttpResponseRedirect('/')
        else:
            messages.warning(vRequest, 'Erro ao responder')
    else:
        form= FormContato()
    
    return render_to_response(
        'briefing/briefing.html',
        locals(),
        context_instance=RequestContext(vRequest),
        )
