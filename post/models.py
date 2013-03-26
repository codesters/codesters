from django.db import models
#from profiles.models import Student

from django.core.urlresolvers import reverse

class Tag(models.Model):
    name = models.CharField(max_length=60)
    slug = models.SlugField(default='')
    help_text = models.CharField(max_length=300, null=True, blank=True)

    def __unicode__(self):
        return self.name

class PostType(models.Model):
    name = models.CharField(max_length=60)
    slug = models.SlugField(default='')
    help_text = models.CharField(max_length=300, null=True, blank=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post_type_list', kwargs={'slug': self.slug})

class Post(models.Model):
    title = models.CharField(max_length=250)
    url = models.URLField()
    post_type = models.ForeignKey(PostType)
    tag = models.ManyToManyField(Tag)
    vote = models.IntegerField(default=0, editable=False)
    posted_by = models.ForeignKey('profiles.Student')
    posted_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.id})
