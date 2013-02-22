from django.db import models
from post.models import Post
from profiles.models import Student, Moderator

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    problem_statement = models.TextField()

    def __unicode__(self):
        return unicode(self.name)

class ExerciseSubmission(models.Model):
    student = models.ForeignKey(Student)
    exercise = models.ForeignKey(Exercise)
    github_url = models.URLField()
    endorse = models.ManyToManyField(Moderator)

    def __unicode__(self):
        return u'%s from %s at %s' % (exercise.name, student.user.username, github_url)

class Lesson(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField(blank=True, default='')
#    ordering = models.IntegerField()
    posts = models.ManyToManyField(Post)
    exercise = models.ForeignKey(Exercise)

    def __unicode__(self):
        return unicode(self.name)

