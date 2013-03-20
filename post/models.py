from django.db import models
#from profiles.models import Student


class Tag(models.Model):
    name = models.CharField(max_length=60)
    help_text = models.CharField(max_length=300, null=True, blank=True)

    def __unicode__(self):
        return unicode(self.name)

class PostType(models.Model):
    name = models.CharField(max_length=60)
    help_text = models.CharField(max_length=300, null=True, blank=True)

    def __unicode__(self):
        return unicode(self.name)

class Post(models.Model):
    title = models.CharField(max_length=250)
    url = models.URLField()
    post_type = models.ForeignKey(PostType)
    tag = models.ManyToManyField(Tag)
    vote = models.IntegerField(default=0, editable=False)
    posted_by = models.ForeignKey('profiles.Student')
    posted_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return unicode(self.title)
