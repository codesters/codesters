from django.db import models
from resources.models import Resource
from django.contrib.auth.models import User

class TrackCategory(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField()
    description = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.name

class Track(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.TextField()
    prerequisites = models.TextField(null=True, blank=True)
    category = models.ForeignKey(TrackCategory)
    related_courses = models.ManyToManyField('self', null=True, blank=True)
    created_by = models.ForeignKey(User, related_name='creator')
    created_at = models.DateTimeField(auto_now=True, editable=False)
    moderators = models.ManyToManyField(User, null=True, blank=True)

    def __unicode__(self):
        return self.name

EXERCISE_TYPE = ['Questions', 'Project']

class Exercise(models.Model):
    title = models.CharField(max_length=100)
    exercise_type = models.CharField(max_length=20, choices=zip(EXERCISE_TYPE, EXERCISE_TYPE))
    problem_statement = models.TextField()

    def __unicode__(self):
        return self.title

#TODO make a Questions model for exercise

class ExerciseSubmission(models.Model):
    student = models.ForeignKey(User)
    exercise = models.ForeignKey(Exercise)
    github_url = models.URLField()
    endorse = models.ManyToManyField(User, related_name='endorser')
    accepted = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s from %s at %s' % (exercise.name, student.user.username, github_url)

class Chapter(models.Model):
#    index = models.IntegerField()
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.TextField(blank=True, default='')
    track = models.ForeignKey(Track)
    resources = models.ManyToManyField(Resource)
    exercise = models.ForeignKey(Exercise, null=True, blank=True)

    def __unicode__(self):
        return self.name

class Badge(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(null=True, blank=True)
    track = models.ForeignKey(Track)

    def __unicode__(self):
        return self.name


