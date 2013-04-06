# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TrackCategory'
        db.create_table('tracks_trackcategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('tracks', ['TrackCategory'])

        # Adding model 'Track'
        db.create_table('tracks_track', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('prerequisites', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tracks.TrackCategory'])),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='creator', to=orm['auth.User'])),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('tracks', ['Track'])

        # Adding M2M table for field related_courses on 'Track'
        db.create_table('tracks_track_related_courses', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_track', models.ForeignKey(orm['tracks.track'], null=False)),
            ('to_track', models.ForeignKey(orm['tracks.track'], null=False))
        ))
        db.create_unique('tracks_track_related_courses', ['from_track_id', 'to_track_id'])

        # Adding M2M table for field moderators on 'Track'
        db.create_table('tracks_track_moderators', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('track', models.ForeignKey(orm['tracks.track'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('tracks_track_moderators', ['track_id', 'user_id'])

        # Adding model 'Exercise'
        db.create_table('tracks_exercise', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('exercise_type', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('problem_statement', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('tracks', ['Exercise'])

        # Adding model 'ExerciseSubmission'
        db.create_table('tracks_exercisesubmission', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('exercise', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tracks.Exercise'])),
            ('github_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('accepted', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('tracks', ['ExerciseSubmission'])

        # Adding M2M table for field endorse on 'ExerciseSubmission'
        db.create_table('tracks_exercisesubmission_endorse', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('exercisesubmission', models.ForeignKey(orm['tracks.exercisesubmission'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('tracks_exercisesubmission_endorse', ['exercisesubmission_id', 'user_id'])

        # Adding model 'Chapter'
        db.create_table('tracks_chapter', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('track', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tracks.Track'])),
            ('exercise', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tracks.Exercise'], null=True, blank=True)),
        ))
        db.send_create_signal('tracks', ['Chapter'])

        # Adding M2M table for field resources on 'Chapter'
        db.create_table('tracks_chapter_resources', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('chapter', models.ForeignKey(orm['tracks.chapter'], null=False)),
            ('resource', models.ForeignKey(orm['resources.resource'], null=False))
        ))
        db.create_unique('tracks_chapter_resources', ['chapter_id', 'resource_id'])

        # Adding model 'Badge'
        db.create_table('tracks_badge', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('track', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tracks.Track'])),
        ))
        db.send_create_signal('tracks', ['Badge'])


    def backwards(self, orm):
        # Deleting model 'TrackCategory'
        db.delete_table('tracks_trackcategory')

        # Deleting model 'Track'
        db.delete_table('tracks_track')

        # Removing M2M table for field related_courses on 'Track'
        db.delete_table('tracks_track_related_courses')

        # Removing M2M table for field moderators on 'Track'
        db.delete_table('tracks_track_moderators')

        # Deleting model 'Exercise'
        db.delete_table('tracks_exercise')

        # Deleting model 'ExerciseSubmission'
        db.delete_table('tracks_exercisesubmission')

        # Removing M2M table for field endorse on 'ExerciseSubmission'
        db.delete_table('tracks_exercisesubmission_endorse')

        # Deleting model 'Chapter'
        db.delete_table('tracks_chapter')

        # Removing M2M table for field resources on 'Chapter'
        db.delete_table('tracks_chapter_resources')

        # Deleting model 'Badge'
        db.delete_table('tracks_badge')


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
        'resources.resource': {
            'Meta': {'object_name': 'Resource'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'resource_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['resources.ResourceType']"}),
            'show': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'topics': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['resources.Topic']", 'symmetrical': 'False'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': '200'}),
            'vote': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'resources.resourcetype': {
            'Meta': {'object_name': 'ResourceType'},
            'color': ('django.db.models.fields.CharField', [], {'default': "'purple'", 'unique': 'True', 'max_length': '20'}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'})
        },
        'resources.topic': {
            'Meta': {'object_name': 'Topic'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'})
        },
        'tracks.badge': {
            'Meta': {'object_name': 'Badge'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'track': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tracks.Track']"})
        },
        'tracks.chapter': {
            'Meta': {'object_name': 'Chapter'},
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'exercise': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tracks.Exercise']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'resources': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['resources.Resource']", 'symmetrical': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'track': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tracks.Track']"})
        },
        'tracks.exercise': {
            'Meta': {'object_name': 'Exercise'},
            'exercise_type': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'problem_statement': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'tracks.exercisesubmission': {
            'Meta': {'object_name': 'ExerciseSubmission'},
            'accepted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'endorse': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'endorser'", 'symmetrical': 'False', 'to': "orm['auth.User']"}),
            'exercise': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tracks.Exercise']"}),
            'github_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'tracks.track': {
            'Meta': {'object_name': 'Track'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tracks.TrackCategory']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'creator'", 'to': "orm['auth.User']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'moderators': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'prerequisites': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'related_courses': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'related_courses_rel_+'", 'null': 'True', 'to': "orm['tracks.Track']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        'tracks.trackcategory': {
            'Meta': {'object_name': 'TrackCategory'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['tracks']