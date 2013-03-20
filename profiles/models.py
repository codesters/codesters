from django.db import models
from django.contrib.auth.models import User
#from track.models import Chapter, Badge

class Student(models.Model):
    user = models.ForeignKey(User)
    bio = models.TextField(blank=True, default='')
    github_username = models.CharField(max_length=30, null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    twitter_username = models.CharField(max_length=30, null=True, blank=True)
    stackoverflow = models.URLField(null=True, blank=True)
    coderwall = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    badges = models.ManyToManyField('track.Badge', null=True, blank=True)
    chapters_completed = models.ManyToManyField('track.Chapter', null=True, blank=True)

    def __unicode__(self):
        return self.user.username

#class Moderator(models.Model):
#    user = models.ForeignKey(User)
#
#    def __unicode__(self):
#        return u'%s' %self.user

#@receiver(user_signed_up)
#def student_create(sender, user, request, **kwargs):
#    s = Student.objects.create(user=user)
#    s.save()
