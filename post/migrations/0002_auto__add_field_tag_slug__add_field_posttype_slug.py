# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Tag.slug'
        db.add_column('post_tag', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default='', max_length=50),
                      keep_default=False)

        # Adding field 'PostType.slug'
        db.add_column('post_posttype', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default='', max_length=50),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Tag.slug'
        db.delete_column('post_tag', 'slug')

        # Deleting field 'PostType.slug'
        db.delete_column('post_posttype', 'slug')


    models = {
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
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'post.post': {
            'Meta': {'object_name': 'Post'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['post.PostType']"}),
            'posted_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['profiles.Student']"}),
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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "''", 'max_length': '50'})
        },
        'post.tag': {
            'Meta': {'object_name': 'Tag'},
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "''", 'max_length': '50'})
        },
        'profiles.student': {
            'Meta': {'object_name': 'Student'},
            'badges': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['track.Badge']", 'null': 'True', 'blank': 'True'}),
            'bio': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'chapters_completed': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['track.Chapter']", 'null': 'True', 'blank': 'True'}),
            'coderwall': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'github_username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'linkedin': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'stackoverflow': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'twitter_username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'track.badge': {
            'Meta': {'object_name': 'Badge'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'track': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['track.Track']"})
        },
        'track.chapter': {
            'Meta': {'object_name': 'Chapter'},
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'exercise': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['track.Exercise']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'posts': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['post.Post']", 'symmetrical': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'track': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['track.Track']"})
        },
        'track.exercise': {
            'Meta': {'object_name': 'Exercise'},
            'exercise_type': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'problem_statement': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'track.track': {
            'Meta': {'object_name': 'Track'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['track.TrackCategory']"}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'creator'", 'to': "orm['profiles.Student']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'moderators': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['profiles.Student']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'prerequisites': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'related_courses': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'related_courses_rel_+'", 'null': 'True', 'to': "orm['track.Track']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        'track.trackcategory': {
            'Meta': {'object_name': 'TrackCategory'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['post']