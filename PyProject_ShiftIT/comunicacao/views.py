# -*- coding: utf-8 -*-
from django.shortcuts                           import render_to_response
from django.template                            import RequestContext
from django.http                                import HttpResponseRedirect
from django.contrib                             import messages

from comunicacao.forms        import FormEmail, FormContato
from comunicacao.controle     import Controle as ComunicacaoControle
from comunicacao.models       import Pergunta_Contato, Resposta_Contato

import datetime
import logging

def contato (vRequest, vTitulo):
    
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
            
            ComunicacaoControle().enviarEmail('[Contato Shift it]', iEmail.mensagem, 'contato@shiftit.com.br', iRemetente) 
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
    try:
        if vRequest.method == 'POST':
            form = FormContato(vRequest.POST)
            if form.is_valid() :
                iContato                = form.save(commit=False)
                iContato.data           = str(datetime.datetime.today())[:19]
                iContato.save()
                for pergunta in iListaPerguntas:
                    if 'resposta_' + str(pergunta.id) in vRequest.POST:
                        iResposta           = Resposta_Contato()
                        iResposta.pergunta  = Pergunta_Contato().obtemPerguntaContato(pergunta.id)
                        iResposta.contato   = iContato
                        iResposta.resposta  = vRequest.POST.get('resposta_' + str(pergunta.id))
                        iResposta.save()
                ComunicacaoControle().enviarEmail('[Briefing Shift it]', 'Recebido Briefing! ;)', 'contato@shiftit.com.br','contato@shiftit.com.br' ) 
                return HttpResponseRedirect('/')
            else:
                messages.warning(vRequest, 'Erro ao responder')
        else:
            form= FormContato()
    except Exception, e:
        logging.getLogger('PyProject_ShiftIT.controle').error('Nao foi possivel view briefing: ' + str(e))
        return HttpResponseRedirect('/')   
    
    return render_to_response(
        'briefing/briefing.html',
        locals(),
        context_instance=RequestContext(vRequest),
        )
