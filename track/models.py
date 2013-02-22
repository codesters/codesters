from django.db import models
from post.models import Post

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    problem_statement = models.TextField()
    github_url = models.URLField()
#endorse

    def __unicode__(self):
        return unicode(self.name)

class Lesson(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField(blank=True, default='')
#    ordering = models.IntegerField()
    posts = models.ManyToManyField(Post)
    exercise = models.ForeignKey(Exercise)

    def __unicode__(self):
        return unicode(self.name)

