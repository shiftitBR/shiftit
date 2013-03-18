from __future__ import with_statement
from fabric.api import local, settings, abort, run, cd, env
from fabric.contrib.console import confirm

import datetime

env.hosts = ['shift@web380.webfaction.com']


def roda_teste():
    with settings(warn_only=True):
        result1 = local('python ./manage.py test autenticacao', capture=True)
        result2 = local('python ./manage.py test bugtracker', capture=True)
        result3 = local('python ./manage.py test comunicacao', capture=True)
    if (result1.failed or result2.failed or result3.failed):
        abort("O teste FALHOU! Abortando...")

def roda_teste_remoto(vDiretorio):
    with settings(warn_only=True):
        with cd(vDiretorio):
            result = run('python2.7 ./manage.py test cadastro')
    if result.failed and not confirm("O teste FALHOU! Continuar mesmo assim?"):
        abort("Abortando...")
  
def cria_tag_master(vNomeTag):
    if vNomeTag == None:
        iNomeTag= 'Producao_%s_%s' % (str(datetime.datetime.today().year), str(datetime.datetime.today().timetuple()[7]))
    else:
        iNomeTag= vNomeTag
    local("git tag %s HEAD" % iNomeTag)

def cria_tag_producao(vNomeTag):
    if vNomeTag == None:
        iNomeTag= 'Deploy_%s_%s' % (str(datetime.datetime.today().year), str(datetime.datetime.today().timetuple()[7]))
    else:
        iNomeTag= vNomeTag
    local("git tag %s HEAD" % iNomeTag)

def push_tag():
    local('git push --tags')

def cria_branch():
    try:
        local('git branch -d producao')
    except:
        pass
    local("git branch producao master")
    
def push_producao():
    local('git push -u origin producao')
    
def checkout(vBranch):
    local('git checkout %s' % vBranch)
    
def pull():
    local('git pull')
    
def fetch():
    local('git fetch')

def fetch_pull_remoto(vDiretorio, vBranch):
    with cd(vDiretorio):
        run('git fetch origin %s' % vBranch)
        run('git pull origin %s' % vBranch)

def clone_producao(vDiretorio):
    try:
        run('rm -r -I %s' % vDiretorio)
        run('mkdir %s' % vDiretorio)
    except:
        pass
    run("git clone https://shiftitBR@github.com/shiftitBR/FreelaTI.com.git %s" % vDiretorio)

def checkout_remoto(vDiretorio):
    with cd(vDiretorio):
        run('git checkout producao')

def sincronizaBanco_remoto(vDiretorio):
    with cd(vDiretorio):
        run('python2.7 %s%s syncdb' % (vDiretorio, 'manage.py'))

def reiniciaApache_remoto(vDiretorio):
    with cd(vDiretorio):
        run('./restart')

def instalaDependencias_remoto(vDiretorio):
    with cd(vDiretorio):
        run('pip-2.7 install --quiet -r ../help/requirements.txt')

def cria_pastaLog(vDiretorio):
    with cd(vDiretorio):
        run('mkdir %s%s' % (vDiretorio, 'log/')) 
        
def copia_settingsLocal(vDiretorioArquivos, vDiretorioApp):
    with cd(vDiretorioArquivos):
        run('cp %s%s %s%s' % (vDiretorioArquivos, 'local_settings.py', vDiretorioApp, 'local_settings.py'))

def merge_branch():
    local('git checkout master')
    local('git merge --no-ff producao')
    roda_teste()
    local('git push -u origin master')
        
#def deploy_producao(vNovaVersao=False, vNomeTag=None):
#    iDiretorioProducao= '/home/shift/webapps/freelati/git/'
#    iDiretorioApache= '/home/shift/webapps/freelati/apache2/bin/'
#    iDiretorioApp= '/home/shift/webapps/freelati/git/PyProject_FreelaTI/src/PyProject_FreelaTI/'
#    iDiretorioArquivos= '/home/shift/webapps/freelati/arquivos/'
#    if vNovaVersao:
#        print '>>>>>>>>>>>>>>>>>>>> Nova versao'
#        checkout('master')
#        pull() #master
#        roda_teste()
#        cria_tag_master(vNomeTag)
#        push_tag() #master
#        cria_branch()
#        push_producao() 
#        cria_tag_producao(vNomeTag)
#        push_tag() #producao
#        clone_producao(iDiretorioProducao)
#        checkout_remoto(iDiretorioProducao)
#        cria_pastaLog(iDiretorioApp)
#        copia_settingsLocal(iDiretorioArquivos, iDiretorioApp)
#    else:
#        print '>>>>>>>>>>>>>>>>>>>> Versao atual'
#        checkout('producao')
#        pull() #producao
#        roda_teste()
#    
#    fetch_pull_remoto(iDiretorioProducao)
#    #roda_teste_remoto(iDiretorioApp)
#    sincronizaBanco_remoto(iDiretorioApp)
#    reiniciaApache_remoto(iDiretorioApache)

def deploy_teste():
    iDiretorioApache= '/home/shift/webapps/teste_shiftit/apache2/bin/'
    iDiretorioApp= '/home/shift/webapps/teste_shiftit/git/PyProject_ShiftIT/PyProject_ShiftIT/'
    fetch()
    checkout('master')
    pull() #master
    roda_teste()    
    fetch_pull_remoto(iDiretorioApp, 'master')
    sincronizaBanco_remoto(iDiretorioApp)
    instalaDependencias_remoto(iDiretorioApp)
    reiniciaApache_remoto(iDiretorioApache)
