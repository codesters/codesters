# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Exercise'
        db.create_table('track_exercise', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('problem_statement', self.gf('django.db.models.fields.TextField')()),
            ('github_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('track', ['Exercise'])

        # Adding model 'Lesson'
        db.create_table('track_lesson', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('about', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('exercise', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['track.Exercise'])),
        ))
        db.send_create_signal('track', ['Lesson'])

        # Adding M2M table for field posts on 'Lesson'
        db.create_table('track_lesson_posts', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('lesson', models.ForeignKey(orm['track.lesson'], null=False)),
            ('post', models.ForeignKey(orm['post.post'], null=False))
        ))
        db.create_unique('track_lesson_posts', ['lesson_id', 'post_id'])


    def backwards(self, orm):
        # Deleting model 'Exercise'
        db.delete_table('track_exercise')

        # Deleting model 'Lesson'
        db.delete_table('track_lesson')

        # Removing M2M table for field posts on 'Lesson'
        db.delete_table('track_lesson_posts')


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
        },
        'track.exercise': {
            'Meta': {'object_name': 'Exercise'},
            'github_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'problem_statement': ('django.db.models.fields.TextField', [], {})
        },
        'track.lesson': {
            'Meta': {'object_name': 'Lesson'},
            'about': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'exercise': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['track.Exercise']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'posts': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['post.Post']", 'symmetrical': 'False'})
        }
    }

    complete_apps = ['track']