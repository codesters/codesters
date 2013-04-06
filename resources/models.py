from django.db import models
from django.contrib.auth.models import User

from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify

LEVELS = ['noob', 'beginner', 'intermediate', 'advanced']

class Topic(models.Model):
    name = models.CharField(max_length=60, unique=True)
    slug = models.SlugField(max_length=255)
    help_text = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('resource_topic_list', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Topic, self).save(*args, **kwargs)

class ResourceType(models.Model):
    name = models.CharField(max_length=60, unique=True)
    slug = models.SlugField(max_length=255)
    help_text = models.CharField(max_length=255, null=True, blank=True)
    color = models.CharField(max_length=20, default='purple', unique=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('resource_type_list', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(ResourceType, self).save(*args, **kwargs)

class Resource(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, blank=True, default='')
    url = models.URLField(unique=True)
    help_text = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True, default='')
    resource_type = models.ForeignKey(ResourceType)
    level = models.CharField(max_length=30, choices=zip(LEVELS, LEVELS))
    topics = models.ManyToManyField(Topic)
    created_by = models.ForeignKey(User)
    vote = models.IntegerField(default=0, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    show = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('resource_detail', kwargs={'pk': self.id})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if self.description and not self.help_text:
            self.help_text = description[:220]
        super(Resource, self).save(*args, **kwargs)

    def upvote(self, number=1):
        self.vote += number
        self.save()

    def downvote(self, number=1):
        self.vote -= number
        self.save()

from guardian.shortcuts import assign_perm
from django.db.models.signals import post_save
def create_resource_permission(sender, instance, created, **kwargs):
    if created:
        from django.contrib.auth.models import Group
        admins = Group.objects.get(name='admins')
        mods = Group.objects.get(name='mods')
        assign_perm('change_resource', instance.created_by, instance)
        assign_perm('delete_resource', instance.created_by, instance)
        assign_perm('change_resource', admins, instance)
        assign_perm('delete_resource', admins, instance)
        assign_perm('change_resource', mods, instance)
        assign_perm('delete_resource', mods, instance)

post_save.connect(create_resource_permission, sender=Resource)
