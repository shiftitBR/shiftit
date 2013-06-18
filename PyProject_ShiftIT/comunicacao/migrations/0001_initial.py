# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Email'
        db.create_table('tb_email', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('telefone', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('mensagem', self.gf('django.db.models.fields.TextField')(max_length=10000)),
            ('data', self.gf('django.db.models.fields.DateTimeField')(null=True)),
        ))
        db.send_create_signal('comunicacao', ['Email'])

        # Adding model 'Contato'
        db.create_table('tb_contato', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('telefone', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('data', self.gf('django.db.models.fields.DateTimeField')(null=True)),
        ))
        db.send_create_signal('comunicacao', ['Contato'])

        # Adding model 'Pergunta_Contato'
        db.create_table('tb_pergunta_contato', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pergunta', self.gf('django.db.models.fields.TextField')(max_length=500)),
        ))
        db.send_create_signal('comunicacao', ['Pergunta_Contato'])

        # Adding model 'Resposta_Contato'
        db.create_table('tb_resposta_contato', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pergunta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['comunicacao.Pergunta_Contato'])),
            ('contato', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['comunicacao.Contato'])),
            ('resposta', self.gf('django.db.models.fields.TextField')(max_length=500)),
        ))
        db.send_create_signal('comunicacao', ['Resposta_Contato'])


    def backwards(self, orm):
        # Deleting model 'Email'
        db.delete_table('tb_email')

        # Deleting model 'Contato'
        db.delete_table('tb_contato')

        # Deleting model 'Pergunta_Contato'
        db.delete_table('tb_pergunta_contato')

        # Deleting model 'Resposta_Contato'
        db.delete_table('tb_resposta_contato')


    models = {
        'comunicacao.contato': {
            'Meta': {'object_name': 'Contato', 'db_table': "'tb_contato'"},
            'data': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'telefone': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        'comunicacao.email': {
            'Meta': {'object_name': 'Email', 'db_table': "'tb_email'"},
            'data': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mensagem': ('django.db.models.fields.TextField', [], {'max_length': '10000'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'telefone': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        'comunicacao.pergunta_contato': {
            'Meta': {'object_name': 'Pergunta_Contato', 'db_table': "'tb_pergunta_contato'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pergunta': ('django.db.models.fields.TextField', [], {'max_length': '500'})
        },
        'comunicacao.resposta_contato': {
            'Meta': {'object_name': 'Resposta_Contato', 'db_table': "'tb_resposta_contato'"},
            'contato': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['comunicacao.Contato']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pergunta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['comunicacao.Pergunta_Contato']"}),
            'resposta': ('django.db.models.fields.TextField', [], {'max_length': '500'})
        }
    }

    complete_apps = ['comunicacao']