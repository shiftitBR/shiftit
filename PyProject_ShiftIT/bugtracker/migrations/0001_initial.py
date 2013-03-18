# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Documento'
        db.create_table('tb_documento', (
            ('id_documento', self.gf('django.db.models.fields.IntegerField')(max_length=3, primary_key=True)),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['autenticacao.Usuario'], blank=True)),
            ('assunto', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('arquivo', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal('bugtracker', ['Documento'])

        # Adding model 'Tipo_Prioridade'
        db.create_table('tb_tipo_prioridade', (
            ('id_tipo_prioridade', self.gf('django.db.models.fields.IntegerField')(max_length=3, primary_key=True)),
            ('descricao', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal('bugtracker', ['Tipo_Prioridade'])

        # Adding model 'Tipo_Estado'
        db.create_table('tb_tipo_estado', (
            ('id_tipo_estado', self.gf('django.db.models.fields.IntegerField')(max_length=3, primary_key=True)),
            ('descricao', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('bugtracker', ['Tipo_Estado'])

        # Adding model 'Bug'
        db.create_table('tb_bug', (
            ('id_bug', self.gf('django.db.models.fields.IntegerField')(max_length=3, primary_key=True)),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['autenticacao.Usuario'], blank=True)),
            ('tipo_prioridade', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bugtracker.Tipo_Prioridade'], blank=True)),
            ('descricao', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('nome_contato', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('email_contato', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('telefone_contato', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('imagem', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('data', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal('bugtracker', ['Bug'])

        # Adding model 'Estado_Bug'
        db.create_table('tb_estado_bug', (
            ('id_estado_bug', self.gf('django.db.models.fields.IntegerField')(max_length=3, primary_key=True)),
            ('bug', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bugtracker.Bug'])),
            ('tipo_estado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bugtracker.Tipo_Estado'])),
            ('comentario', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('data', self.gf('django.db.models.fields.DateTimeField')(null=True)),
        ))
        db.send_create_signal('bugtracker', ['Estado_Bug'])

        # Adding model 'Pergunta_Bug'
        db.create_table('tb_pergunta_bug', (
            ('id_pergunta_bug', self.gf('django.db.models.fields.IntegerField')(max_length=3, primary_key=True)),
            ('pergunta', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal('bugtracker', ['Pergunta_Bug'])

        # Adding model 'Resposta_Bug'
        db.create_table('tb_resposta_bug', (
            ('id_resposta_bug', self.gf('django.db.models.fields.IntegerField')(max_length=3, primary_key=True)),
            ('pergunta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bugtracker.Pergunta_Bug'])),
            ('bug', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bugtracker.Bug'])),
            ('resposta', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal('bugtracker', ['Resposta_Bug'])


    def backwards(self, orm):
        # Deleting model 'Documento'
        db.delete_table('tb_documento')

        # Deleting model 'Tipo_Prioridade'
        db.delete_table('tb_tipo_prioridade')

        # Deleting model 'Tipo_Estado'
        db.delete_table('tb_tipo_estado')

        # Deleting model 'Bug'
        db.delete_table('tb_bug')

        # Deleting model 'Estado_Bug'
        db.delete_table('tb_estado_bug')

        # Deleting model 'Pergunta_Bug'
        db.delete_table('tb_pergunta_bug')

        # Deleting model 'Resposta_Bug'
        db.delete_table('tb_resposta_bug')


    models = {
        'autenticacao.usuario': {
            'Meta': {'object_name': 'Usuario', 'db_table': "'tb_usuario'", '_ormbases': ['auth.User']},
            'cidade': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'cnpj': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'endereco': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'nome_fantasia': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'nome_responsavel': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'razao_social': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '500', 'blank': 'True'}),
            'telefone': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'uf': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True', 'primary_key': 'True'})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'bugtracker.bug': {
            'Meta': {'object_name': 'Bug', 'db_table': "'tb_bug'"},
            'data': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'email_contato': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id_bug': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'primary_key': 'True'}),
            'imagem': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'nome_contato': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'telefone_contato': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'tipo_prioridade': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bugtracker.Tipo_Prioridade']", 'blank': 'True'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['autenticacao.Usuario']", 'blank': 'True'})
        },
        'bugtracker.documento': {
            'Meta': {'object_name': 'Documento', 'db_table': "'tb_documento'"},
            'arquivo': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'assunto': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id_documento': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'primary_key': 'True'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['autenticacao.Usuario']", 'blank': 'True'})
        },
        'bugtracker.estado_bug': {
            'Meta': {'object_name': 'Estado_Bug', 'db_table': "'tb_estado_bug'"},
            'bug': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bugtracker.Bug']"}),
            'comentario': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'data': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'id_estado_bug': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'primary_key': 'True'}),
            'tipo_estado': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bugtracker.Tipo_Estado']"})
        },
        'bugtracker.pergunta_bug': {
            'Meta': {'object_name': 'Pergunta_Bug', 'db_table': "'tb_pergunta_bug'"},
            'id_pergunta_bug': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'primary_key': 'True'}),
            'pergunta': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        'bugtracker.resposta_bug': {
            'Meta': {'object_name': 'Resposta_Bug', 'db_table': "'tb_resposta_bug'"},
            'bug': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bugtracker.Bug']"}),
            'id_resposta_bug': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'primary_key': 'True'}),
            'pergunta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bugtracker.Pergunta_Bug']"}),
            'resposta': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        'bugtracker.tipo_estado': {
            'Meta': {'object_name': 'Tipo_Estado', 'db_table': "'tb_tipo_estado'"},
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id_tipo_estado': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'primary_key': 'True'})
        },
        'bugtracker.tipo_prioridade': {
            'Meta': {'object_name': 'Tipo_Prioridade', 'db_table': "'tb_tipo_prioridade'"},
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id_tipo_prioridade': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'primary_key': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['bugtracker']