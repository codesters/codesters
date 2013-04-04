from django.db import models
from django.contrib.auth.models import User

from django.core.urlresolvers import reverse

class Tag(models.Model):
    name = models.CharField(max_length=60, unique=True)
    slug = models.SlugField(default='')
    help_text = models.CharField(max_length=300, null=True, blank=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('feed_tag_list', kwargs={'slug': self.slug})

class FeedType(models.Model):
    name = models.CharField(max_length=60, unique=True)
    slug = models.SlugField(default='')
    help_text = models.CharField(max_length=300, null=True, blank=True)
    color = models.CharField(max_length=20, default='purple', unique=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('feed_type_list', kwargs={'slug': self.slug})

class Feed(models.Model):
    title = models.CharField(max_length=250, unique=True)
    url = models.URLField(unique=True)
    description = models.TextField(null=True, blank=True, default='')
    feed_type = models.ForeignKey(FeedType)
    tags = models.ManyToManyField(Tag)
    vote = models.IntegerField(default=0, editable=False)
    created_by = models.ForeignKey(User)
    created_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('feed_detail', kwargs={'pk': self.id})

    def upvote(self, number=1):
        self.vote += number
        self.save()

    def downvote(self, number=1):
        self.vote -= number
        self.save()
