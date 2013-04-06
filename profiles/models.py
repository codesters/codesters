from django.db import models
from django.contrib.auth.models import User
#from tracks.models import Chapter, Badge

from django.core.urlresolvers import reverse

from django.dispatch import receiver
from registration.signals import user_activated

@receiver(user_activated)
def create_user_profile(sender, user, request, **kwargs):
    from blogs.models import Blog
    user_profile = UserProfile.objects.create(user=user)
    blog_title = str(user.username)+'\'s Blog'
    blog = Blog.objects.create(user=user, title=blog_title)

# make a project model and add user projects field as foreign key
# add a textfield for storing all social profiles at one place and write a method that returns a dict of provider with profile
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    bio = models.TextField(blank=True, default='')
    social = models.TextField(blank=True, default='')
    github = models.CharField(max_length=30, null=True, blank=True)
    twitter = models.CharField(max_length=30, null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    stackoverflow = models.URLField(null=True, blank=True)
    coderwall = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
#    badges = models.ManyToManyField(Badge, null=True, blank=True)
#    chapters_completed = models.ManyToManyField(Chapter, null=True, blank=True)

    def __unicode__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('user_detail', kwargs={'pk': self.user.pk})


from guardian.shortcuts import assign_perm
from django.db.models.signals import post_save
def create_user_permissions(sender, instance, created, **kwargs):
    if created:
        from django.contrib.auth.models import Group
        admins = Group.objects.get(name='admins')
        mods = Group.objects.get(name='mods')
        assign_perm('change_userprofile', instance.user, instance)
        assign_perm('delete_userprofile', instance.user, instance)
        assign_perm('change_user', instance.user, instance.user)
        assign_perm('change_userprofile', admins, instance)
        assign_perm('delete_userprofile', admins, instance)
        assign_perm('change_user', admins, instance.user)
        assign_perm('change_userprofile', mods, instance)
        assign_perm('delete_userprofile', mods, instance)
        assign_perm('change_user', mods, instance.user)

post_save.connect(create_user_permissions, sender=UserProfile)
