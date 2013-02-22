# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tag'
        db.create_table('post_tag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('help_text', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal('post', ['Tag'])

        # Adding model 'PostType'
        db.create_table('post_posttype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('help_text', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal('post', ['PostType'])

        # Adding model 'Post'
        db.create_table('post_post', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('post_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['post.PostType'])),
            ('vote', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('posted_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('post', ['Post'])

        # Adding M2M table for field tag on 'Post'
        db.create_table('post_post_tag', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('post', models.ForeignKey(orm['post.post'], null=False)),
            ('tag', models.ForeignKey(orm['post.tag'], null=False))
        ))
        db.create_unique('post_post_tag', ['post_id', 'tag_id'])


    def backwards(self, orm):
        # Deleting model 'Tag'
        db.delete_table('post_tag')

        # Deleting model 'PostType'
        db.delete_table('post_posttype')

        # Deleting model 'Post'
        db.delete_table('post_post')

        # Removing M2M table for field tag on 'Post'
        db.delete_table('post_post_tag')


    models = {
        'post.post': {
            'Meta': {'object_name': 'Post'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['post.PostType']"}),
            'posted_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'tag': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['post.Tag']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'vote': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'post.posttype': {
            'Meta': {'object_name': 'PostType'},
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'post.tag': {
            'Meta': {'object_name': 'Tag'},
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        }
    }

    complete_apps = ['post']