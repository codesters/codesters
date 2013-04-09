from django.db import models
from django.contrib.auth.models import User
#from tracks.models import Chapter, Badge

from django.core.urlresolvers import reverse

#from django.dispatch import receiver
#from registration.signals import user_activated
#
#@receiver(user_activated)
#def create_user_profile(sender, user, request, **kwargs):
#    user_profile = UserProfile.objects.create(user=user)

#TODO make a project model and add user projects field as foreign key
class Project(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(blank=True, null=True)
    url = models.URLField(unique=True)
    source_url = models.URLField(unique=True, null=True, blank=True)
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
    published = models.BooleanField(default=True)
    user = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __unicode__(self):
        return self.title



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


#from guardian.shortcuts import assign_perm
#from django.db.models.signals import post_save
#def create_user_permissions(sender, instance, created, **kwargs):
#    if created:
#        from django.contrib.auth.models import Group
#        admins = Group.objects.get(name='admins')
#        mods = Group.objects.get(name='mods')
#        assign_perm('change_userprofile', instance.user, instance)
#        assign_perm('delete_userprofile', instance.user, instance)
#        assign_perm('change_user', instance.user, instance.user)
#        assign_perm('change_userprofile', admins, instance)
#        assign_perm('delete_userprofile', admins, instance)
#        assign_perm('change_user', admins, instance.user)
#        assign_perm('change_userprofile', mods, instance)
#        assign_perm('delete_userprofile', mods, instance)
#        assign_perm('change_user', mods, instance.user)
#
#post_save.connect(create_user_permissions, sender=UserProfile)
