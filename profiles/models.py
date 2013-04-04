from django.db import models
from django.contrib.auth.models import User
from tracks.models import Chapter, Badge

from django.core.urlresolvers import reverse

from django.dispatch import receiver
from registration.signals import user_activated

@receiver(user_activated)
def create_user_profile(sender, user, request, **kwargs):
    from blogs.models import Blog
    user_profile = UserProfile.objects.create(user=user)
    blog_title = str(user.username)+'\'s Blog'
    blog = Blog.objects.create(user=user, title=blog_title)

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    bio = models.TextField(blank=True, default='')
    github = models.CharField(max_length=30, null=True, blank=True)
    twitter = models.CharField(max_length=30, null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    stackoverflow = models.URLField(null=True, blank=True)
    coderwall = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    badges = models.ManyToManyField(Badge, null=True, blank=True)
    chapters_completed = models.ManyToManyField(Chapter, null=True, blank=True)

    def __unicode__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('user_detail', kwargs={'pk': self.user.pk})

    def get_feeds(self):
        return self.user.feed_set.all()

    def get_feeds_by_type(self, slug):
        return self.user.feed_set.filter(feed_type__slug=slug)

    def get_feeds_by_tag(self, slug):
        return self.user.feed_set.filter(tags__slug=slug)

    def get_blog(self):
        return self.user.blog

    def get_entries(self):
        return self.user.blog.entry_set.all()

    def get_published_entries(self):
        return self.user.blog.entry_set.filter(published=True)

    def get_entries_by_tag(self, slug):
        return self.user.blog.entry_set.filter(tags__slug=slug)
