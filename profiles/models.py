from django.db import models
from django.contrib.auth.models import User
from resources.models import Topic, Resource
from django.core.urlresolvers import reverse
from django.dispatch import receiver
from registration.signals import user_activated

@receiver(user_activated)
def create_user_profile(sender, user, request, **kwargs):
    user_profile = UserProfile.objects.create(user=user)
    from guardian.shortcuts import assign_perm
    assign_perm('change_userprofile', user, user_profile)
    assign_perm('delete_userprofile', user, user_profile)
    assign_perm('change_user', user, user)

#TODO make a project model and add user projects field as foreign key
class Project(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(blank=True, null=True)
    url = models.URLField()
    source_url = models.URLField(null=True, blank=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.title


class Badge(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=255, blank=True, default='')
    help_text = models.CharField(max_length=220)
    description = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.name


class Snippet(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    show = models.BooleanField(default=True)
    user = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('snippet_detail', kwargs={'pk': self.pk})



#TODO add a textfield for storing all social profiles at one place and write a method that returns a dict of provider with profile
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    bio = models.TextField(blank=True, default='')
    gravatar_email = models.EmailField(null=True, blank=True)
    github = models.CharField('Github Username', max_length=30, null=True, blank=True)
    twitter = models.CharField('Twitter Username', max_length=30, null=True, blank=True)
    stackoverflow = models.CharField('Stackoverflow Profile', max_length=30, null=True, blank=True)
    facebook = models.CharField('Facebook Username', max_length=30, null=True, blank=True)
    website = models.URLField('Your Website/Blog', null=True, blank=True)
    badges = models.ManyToManyField(Badge, null=True, blank=True)

    def __unicode__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('user_detail', kwargs={'username': self.user.username})


class SavedResource(models.Model):
    user = models.ForeignKey(User)
    resource = models.ForeignKey(Resource)
    saved_at = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        unique_together = (('user', 'resource'),)

    def __unicode__(self):
        return '%s %s' %(self.user, self.resource)

class TopicFollow(models.Model):
    user = models.ForeignKey(User)
    topic = models.ForeignKey(Topic)
    followed_at = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        unique_together = (('user','topic'),)

    def __unicode__(self):
        return '%s %s' %(self.user, self.topic)
