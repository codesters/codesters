from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.template.defaultfilters import slugify


class Blog(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'username': self.user.username})


class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=255)

    def __unicode__(self):
         return self.name


class Entry(models.Model):
    blog = models.ForeignKey(Blog)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    content = models.TextField()
    tags = models.ManyToManyField(Tag, null=True, blank=True)
    published = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('entry_detail', kwargs={'username':self.blog.user.username, 'slug': self.slug})
