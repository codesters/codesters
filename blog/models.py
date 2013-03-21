from django.contrib.auth.models import User
from django.db import models
from profiles.models import Student
from django.template.defaultfilters import slugify

class Blog(models.Model):
    student = models.ForeignKey(Student)
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return self.title

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
    tags = models.ManyToManyField(Tag)
    published = models.BooleanField(default=True)
    author = models.ForeignKey(User, related_name='entrys')

    def __unicode__(self):
        return self.title

#    def save(self, *args, **kwargs):
#        if not self.slug:
#            self.slug == slugify(self.title)
#        self(Entry, self).save(*args, **kwargs)
