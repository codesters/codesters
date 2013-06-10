from django.db import models
from django.contrib.auth.models import User
from resources.models import Topic, Resource
from django.core.urlresolvers import reverse

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
        return reverse('snippet_detail', kwargs={'username': self.user.username, 'pk': self.pk})



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
    receive_email = models.BooleanField(default=True)

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

#SIGNALS

from django.dispatch import receiver
from guardian.shortcuts import assign_perm
from django.db.models.signals import post_save
from django.contrib.auth.signals import user_logged_in
from registration.signals import user_activated

@receiver(user_activated)
def create_user_profile(sender, user, request, **kwargs):
    user_profile = UserProfile.objects.create(user=user)
    from guardian.shortcuts import assign_perm
    assign_perm('change_userprofile', user, user_profile)
    assign_perm('delete_userprofile', user, user_profile)
    assign_perm('change_user', user, user)

def check_userprofile_details(sender, request, user, **kwargs):
    if not user.first_name:
        request.session['no_name'] = True
    topic_list = TopicFollow.objects.filter(user=user)
    if not topic_list:
        request.session['no_topic'] = True

def create_project_permission(sender, instance, created, **kwargs):
    if created:
        assign_perm('change_project', instance.user, instance)
        assign_perm('delete_project', instance.user, instance)

def create_snippet_permission(sender, instance, created, **kwargs):
    if created:
        assign_perm('change_snippet', instance.user, instance)
        assign_perm('delete_snippet', instance.user, instance)

user_logged_in.connect(check_userprofile_details)
post_save.connect(create_snippet_permission, sender=Snippet)
post_save.connect(create_project_permission, sender=Project)
