from django.db import models
from django.contrib.auth.models import User

from allauth.account.signals import user_signed_up
from django.dispatch import receiver

class Student(models.Model):
    user = models.ForeignKey(User)
    bio = models.TextField(blank=True, default='')
    website = models.URLField(null=True, blank=True)

    def __unicode__(self):
        return u'%s' %self.user.get_full_name()

class Moderator(models.Model):
    user = models.ForeignKey(User)

    def __unicode__(self):
        return u'%s' %self.user

@receiver(user_signed_up)
def student_create(sender, user, request, **kwargs):
    s = Student.objects.create(user=user)
    s.save()
