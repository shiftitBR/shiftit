# -*- coding: utf-8 -*-
from django.shortcuts                       import render_to_response
from django.template                        import RequestContext
from django.contrib.auth                    import authenticate 
from django.contrib.auth                    import logout as auth_logout
from django.contrib.auth                    import login as auth_login
from django.http                            import HttpResponseRedirect
from django.contrib                         import messages
from django.contrib.auth.decorators         import login_required

import oControle

def login(vRequest, vTitulo):
    
    if vRequest.POST:
        try:
            username= vRequest.POST.get('login')
            password= vRequest.POST.get('senha')
                
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(vRequest, user)
                vRequest.session.set_expiry(6000)
                return HttpResponseRedirect('/painel_de_controle/')
            else:
                messages.warning(vRequest, 'E-mail e/ou Senha incorreto(s). Digite novamente seu E-mail e Senha para efetuar o login.')
                return HttpResponseRedirect('/login/')
        except Exception, e:
            oControle.getLogger().error('Nao foi possivel get login: ' + str(e))
            return False
    return render_to_response(
        'login/login.html',
        locals(),
        context_instance=RequestContext(vRequest),
        )

@login_required    
def logout(vRequest, vTitulo):
    
    auth_logout(vRequest)
    return HttpResponseRedirect('/')

    return render_to_response(
        'logout/logout.html',
        locals(),
        context_instance=RequestContext(vRequest),
        )