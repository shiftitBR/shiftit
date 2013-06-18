# -*- coding: utf-8 -*-
from django.shortcuts                           import render_to_response
from django.template                            import RequestContext
from django.contrib.auth.decorators             import login_required
from django.http                                import HttpResponseRedirect
from django.contrib                             import messages

from PyProject_ShiftIT.bugtracker.forms         import FormBug
from PyProject_ShiftIT.bugtracker.models        import Pergunta_Bug,\
    Tipo_Prioridade, Resposta_Bug, Estado_Bug

import datetime
from PyProject_ShiftIT.autenticacao.models import Usuario

@login_required   
def adicionar_bug(vRequest, vTitulo):
    
    iUsuario        = Usuario().obtemUsuario(vRequest.user.id)
    iListaPerguntas = Pergunta_Bug.objects.all()
    
    if vRequest.method == 'POST':
        form = FormBug(vRequest.POST, vRequest.FILES)
        
        if form.is_valid() :
            iBug                    = form.save(commit=False)
            iBug.usuario            = iUsuario
            iBug.data               = str(datetime.datetime.today())[:19]
            iBug.tipo_prioridade    = Tipo_Prioridade().obtemTipoPrioridade(vRequest.POST.get('tipo_prioridade'))
            iBug.save()
            for pergunta in iListaPerguntas:
                if 'resposta_' + str(pergunta.id) in vRequest.POST:
                    iResposta           = Resposta_Bug()
                    iResposta.pergunta  = Pergunta_Bug().obtemPerguntaBug(pergunta.id)
                    iResposta.bug       = iBug
                    iResposta.resposta  = vRequest.POST.get('resposta_' + str(pergunta.id))
                    iResposta.save()
            return HttpResponseRedirect('/painel_de_controle/')
        else:
            messages.warning(vRequest, 'Erro ao responder')
    else:
        form= FormBug()
        
    return render_to_response(
        'bug/adicionar_bug.html',
        locals(),
        context_instance=RequestContext(vRequest),
        )
    
@login_required   
def documentos(vRequest, vTitulo):
    

    return render_to_response(
        'documentos/documentos.html',
        locals(),
        context_instance=RequestContext(vRequest),
        )
    
@login_required   
def painel_controle(vRequest, vTitulo):
    iUsuario        = Usuario().obtemUsuario(vRequest.user.id)
    iListaBug       = Estado_Bug().obtemListaBugsAux(iUsuario)

    return render_to_response(
        'painel_controle/painel_controle.html',
        locals(),
        context_instance=RequestContext(vRequest),
        )