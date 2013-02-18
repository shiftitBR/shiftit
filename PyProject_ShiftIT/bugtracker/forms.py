# -*- coding: utf-8 -*-
'''
Created on Mar 5, 2012

@author: Shift IT | www.shiftit.com.br
'''

from django                                     import forms
from PyProject_ShiftIT.bugtracker.models        import Bug, Tipo_Prioridade


class FormBug(forms.ModelForm):
    tipo_prioridade         = forms.ChoiceField(choices=[])
    descricao               = forms.Field(widget=forms.Textarea)
    nome_contato            = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Digite o seu Nome'}))
    email_contato           = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Digite o seu E-mail'}))
    telefone_contato        = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Digite o seu Telefone'}))
    imagem                  = forms.FileField(label='Selecione a Imagem para Avatar', help_text='Avatar')
    
    class Meta:
        model = Bug
        fields = ( 'descricao', 'nome_contato', 'email_contato', 'telefone_contato', 'imagem' ) 
    
    def clean_tipo_prioridade(self):
        if self.cleaned_data['tipo_prioridade'] == '':
            raise forms.ValidationError('O campo Tipo de Prioridade é obrigatório')
        return self.cleaned_data['tipo_prioridade']
    
    def clean_descricao(self):
        if self.cleaned_data['descricao'] == '':
            raise forms.ValidationError('O campo Descrição é obrigatório')
        return self.cleaned_data['descricao'].encode('utf-8')
    
    def clean_nome_contato(self):
        if self.cleaned_data['nome_contato'] == '':
            raise forms.ValidationError('O campo Nome é obrigatório')
        return self.cleaned_data['nome_contato']
    
    def clean_email_contatol(self):
        if self.cleaned_data['email_contato'] == '':
            raise forms.ValidationError('O campo E-mail é obrigatório')
        return self.cleaned_data['email_contato']
    
    def clean_telefone_contato(self):
        if self.cleaned_data['telefone_contato'] == '':
            raise forms.ValidationError('O campo Telefone é obrigatório')
        return self.cleaned_data['telefone_contato']

    def clean_imagem(self):
        return self.cleaned_data['imagem']
    
    def __init__(self, *args, **kwargs):
        
        iListaTipoPrioridade = Tipo_Prioridade().obtemListaTipoPrioridade()
        iLista = []
        for tipoprioridade in iListaTipoPrioridade:
            iLista.append((str(tipoprioridade.id_tipo_prioridade), str(tipoprioridade.descricao)))
        
        super(FormBug, self).__init__(*args, **kwargs)
        self.fields['tipo_prioridade'].error_messages['required']   = u'O campo Tipo de Prioridade é obrigatório'
        self.fields['descricao'].error_messages['required']         = u'O campo Descrição é obrigatório'
        self.fields['nome_contato'].error_messages['required']      = u'O campo Nome é obrigatório'
        self.fields['email_contato'].error_messages['required']     = u'O campo E-mail é obrigatório'
        self.fields['telefone_contato'].error_messages['required']  = u'O campo Telefone é obrigatório'
        self.fields['imagem'].required                              = False
        self.fields['tipo_prioridade'].choices                      = iLista
        
    def save(self, commit=True):
        bug = super(FormBug, self).save(commit=False)
        if commit:
            bug.save()
        return bug 
