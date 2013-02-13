# -*- coding: utf-8 -*-
'''
Created on Mar 5, 2012

@author: Shift IT | www.shiftit.com.br
'''

from django                                     import forms
from PyProject_ShiftIT.comunicacao.models       import Email


class FormEmail(forms.ModelForm):
    nome        = forms.CharField(max_length=50)
    email       = forms.EmailField(required=False)
    telefone    = forms.CharField(max_length=50)
    mensagem    = forms.Field(widget=forms.Textarea)
    
    class Meta:
        model = Email
        fields = ('nome', 'email', 'telefone', 'mensagem', ) 
    
    def clean_nome(self):
        if self.cleaned_data['nome'] == '':
            raise forms.ValidationError('O campo Nome é obrigatório')
        return self.cleaned_data['nome']
    
    def clean_email(self):
        if self.cleaned_data['email'] == '':
            raise forms.ValidationError('O campo E-mail é obrigatório')
        return self.cleaned_data['email']
    
    def clean_telefone(self):
        if self.cleaned_data['telefone'] == '':
            raise forms.ValidationError('O campo Telefone é obrigatório')
        return self.cleaned_data['telefone']
    
    def clean_mensagem(self):
        if self.cleaned_data['mensagem'] == '':
            raise forms.ValidationError('O campo Mensagem é obrigatório')
        return self.cleaned_data['mensagem']
    
    def __init__(self, *args, **kwargs):
        super(FormEmail, self).__init__(*args, **kwargs)
        self.fields['email'].error_messages['required'] = u'O campo E-mail é obrigatório'
        self.fields['nome'].error_messages['required'] = u'O campo Nome é obrigatório'
        self.fields['mensagem'].error_messages['required'] = u'O campo Mensagem é obrigatório'
        self.fields['telefone'].error_messages['required'] = u'O campo Telefone é obrigatório'
        