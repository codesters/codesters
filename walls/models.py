from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.template.defaultfilters import slugify


class Wall(models.Model):
    user = models.OneToOneField(User)
    title = models.CharField(max_length=60)
    slug = models.SlugField(max_length=255, blank=True, default='')
    subtitle = models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('wall_detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Wall, self).save(*args, **kwargs)

class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=255)

    def __unicode__(self):
         return self.name


class Snippet(models.Model):
    wall = models.ForeignKey(Wall)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True, default='')
    content = models.TextField()
    tags = models.ManyToManyField(Tag, null=True, blank=True)
    published = models.BooleanField(default=True)
    created_by = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('snippet_detail', kwargs={'pk':self.pk})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        self.created_by = self.wall.user # makes sure that created_by is the wall owner
        super(Snippet, self).save(*args, **kwargs)


from guardian.shortcuts import assign_perm
from django.db.models.signals import post_save
def create_wall_permissions(sender, instance, created, **kwargs):
    if created:
        from django.contrib.auth.models import Group
        admins = Group.objects.get(name='admins')
        mods = Group.objects.get(name='mods')
        assign_perm('change_wall', instance.user, instance)
        assign_perm('delete_wall', instance.user, instance)
        assign_perm('change_wall', admins, instance)
        assign_perm('delete_wall', admins, instance)
        assign_perm('change_wall', mods, instance)
        assign_perm('delete_wall', mods, instance)

def create_snippet_permissions(sender, instance, created, **kwargs):
    if created:
        from django.contrib.auth.models import Group
        admins = Group.objects.get(name='admins')
        mods = Group.objects.get(name='mods')
        assign_perm('change_snippet', instance.wall.user, instance)
        assign_perm('delete_snippet', instance.wall.user, instance)
        assign_perm('change_snippet', admins, instance)
        assign_perm('delete_snippet', admins, instance)
        assign_perm('change_snippet', mods, instance)
        assign_perm('delete_snippet', mods, instance)

post_save.connect(create_snippet_permissions, sender=Snippet)
post_save.connect(create_wall_permissions, sender=Wall)
