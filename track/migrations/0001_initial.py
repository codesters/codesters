# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TrackCategory'
        db.create_table('track_trackcategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('track', ['TrackCategory'])

        # Adding model 'Track'
        db.create_table('track_track', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('prerequisites', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['track.TrackCategory'])),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='creator', to=orm['profiles.Student'])),
        ))
        db.send_create_signal('track', ['Track'])

        # Adding M2M table for field related_courses on 'Track'
        db.create_table('track_track_related_courses', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_track', models.ForeignKey(orm['track.track'], null=False)),
            ('to_track', models.ForeignKey(orm['track.track'], null=False))
        ))
        db.create_unique('track_track_related_courses', ['from_track_id', 'to_track_id'])

        # Adding M2M table for field moderators on 'Track'
        db.create_table('track_track_moderators', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('track', models.ForeignKey(orm['track.track'], null=False)),
            ('student', models.ForeignKey(orm['profiles.student'], null=False))
        ))
        db.create_unique('track_track_moderators', ['track_id', 'student_id'])

        # Adding model 'Exercise'
        db.create_table('track_exercise', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('exercise_type', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('problem_statement', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('track', ['Exercise'])

        # Adding model 'ExerciseSubmission'
        db.create_table('track_exercisesubmission', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['profiles.Student'])),
            ('exercise', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['track.Exercise'])),
            ('github_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('accepted', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('track', ['ExerciseSubmission'])

        # Adding M2M table for field endorse on 'ExerciseSubmission'
        db.create_table('track_exercisesubmission_endorse', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('exercisesubmission', models.ForeignKey(orm['track.exercisesubmission'], null=False)),
            ('student', models.ForeignKey(orm['profiles.student'], null=False))
        ))
        db.create_unique('track_exercisesubmission_endorse', ['exercisesubmission_id', 'student_id'])

        # Adding model 'Chapter'
        db.create_table('track_chapter', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('track', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['track.Track'])),
            ('exercise', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['track.Exercise'], null=True, blank=True)),
        ))
        db.send_create_signal('track', ['Chapter'])

        # Adding M2M table for field posts on 'Chapter'
        db.create_table('track_chapter_posts', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('chapter', models.ForeignKey(orm['track.chapter'], null=False)),
            ('post', models.ForeignKey(orm['post.post'], null=False))
        ))
        db.create_unique('track_chapter_posts', ['chapter_id', 'post_id'])

        # Adding model 'Badge'
        db.create_table('track_badge', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('track', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['track.Track'])),
        ))
        db.send_create_signal('track', ['Badge'])


    def backwards(self, orm):
        # Deleting model 'TrackCategory'
        db.delete_table('track_trackcategory')

        # Deleting model 'Track'
        db.delete_table('track_track')

        # Removing M2M table for field related_courses on 'Track'
        db.delete_table('track_track_related_courses')

        # Removing M2M table for field moderators on 'Track'
        db.delete_table('track_track_moderators')

        # Deleting model 'Exercise'
        db.delete_table('track_exercise')

        # Deleting model 'ExerciseSubmission'
        db.delete_table('track_exercisesubmission')

        # Removing M2M table for field endorse on 'ExerciseSubmission'
        db.delete_table('track_exercisesubmission_endorse')

        # Deleting model 'Chapter'
        db.delete_table('track_chapter')

        # Removing M2M table for field posts on 'Chapter'
        db.delete_table('track_chapter_posts')

        # Deleting model 'Badge'
        db.delete_table('track_badge')


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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'post.tag': {
            'Meta': {'object_name': 'Tag'},
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'profiles.student': {
            'Meta': {'object_name': 'Student'},
            'badges': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['track.Badge']", 'symmetrical': 'False'}),
            'bio': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'chapters_completed': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['track.Chapter']", 'symmetrical': 'False'}),
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
        'track.exercisesubmission': {
            'Meta': {'object_name': 'ExerciseSubmission'},
            'accepted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'endorse': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'endorser'", 'symmetrical': 'False', 'to': "orm['profiles.Student']"}),
            'exercise': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['track.Exercise']"}),
            'github_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['profiles.Student']"})
        },
        'track.track': {
            'Meta': {'object_name': 'Track'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['track.TrackCategory']"}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'creator'", 'to': "orm['profiles.Student']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'moderators': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['profiles.Student']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'prerequisites': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'related_courses': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'related_courses_rel_+'", 'to': "orm['track.Track']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        'track.trackcategory': {
            'Meta': {'object_name': 'TrackCategory'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['track']