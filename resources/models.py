from django.db import models
from django.contrib.auth.models import User
from djangoratings.fields import RatingField

from django.core.urlresolvers import reverse
from codesters.utils import unique_slugify
from django.template.defaultfilters import slugify

LEVELS = ['beginner', 'intermediate', 'advanced']

class Topic(models.Model):
    name = models.CharField(max_length=60, unique=True)
    slug = models.SlugField(max_length=255)
    help_text = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    thumbnail = models.ImageField(upload_to='topics', null=True, blank=True)
    official_website = models.URLField(null=True, blank=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('resource_topic_home', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        if self.description and not self.help_text:
            self.help_text = self.description[:220]
        super(Topic, self).save(*args, **kwargs)

class ResourceType(models.Model):
    name = models.CharField(max_length=60, unique=True)
    slug = models.SlugField(max_length=255)
    help_text = models.CharField(max_length=255, null=True, blank=True)
    color = models.CharField(max_length=20, default='purple', unique=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('resource_list', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(ResourceType, self).save(*args, **kwargs)

class Resource(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, blank=True, default='')
    url = models.URLField(verify_exists=True, unique=True)
    help_text = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True, default='')
    resource_type = models.ForeignKey(ResourceType)
    level = models.CharField(max_length=30, choices=zip(LEVELS, LEVELS))
    topics = models.ManyToManyField(Topic)
    created_by = models.ForeignKey(User)
    rating = RatingField(range=5, weight=10, use_cookies=True, allow_delete=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    show = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('resource_detail', kwargs={'pk': self.id})

    def save(self, *args, **kwargs):
        #INFO Checks if present because admins have option to change slug
        if not self.slug:
            slug_str = '%s' % self.title
            unique_slugify(self, slug_str)
        if self.description and not self.help_text:
            self.help_text = self.description[:220]
        super(Resource, self).save(*args, **kwargs)


from guardian.shortcuts import assign_perm
from django.db.models.signals import post_save
def create_resource_permission(sender, instance, created, **kwargs):
    if created:
        assign_perm('change_resource', instance.created_by, instance)
        assign_perm('delete_resource', instance.created_by, instance)

post_save.connect(create_resource_permission, sender=Resource)
