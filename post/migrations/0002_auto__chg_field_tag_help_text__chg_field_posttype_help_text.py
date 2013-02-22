# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Tag.help_text'
        db.alter_column('post_tag', 'help_text', self.gf('django.db.models.fields.CharField')(max_length=300, null=True))

        # Changing field 'PostType.help_text'
        db.alter_column('post_posttype', 'help_text', self.gf('django.db.models.fields.CharField')(max_length=300, null=True))

    def backwards(self, orm):

        # Changing field 'Tag.help_text'
        db.alter_column('post_tag', 'help_text', self.gf('django.db.models.fields.CharField')(default=None, max_length=300))

        # Changing field 'PostType.help_text'
        db.alter_column('post_posttype', 'help_text', self.gf('django.db.models.fields.CharField')(default='help-text', max_length=300))

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
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'post.tag': {
            'Meta': {'object_name': 'Tag'},
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        }
    }

    complete_apps = ['post']