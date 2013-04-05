from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.template.defaultfilters import slugify


class Blog(models.Model):
    user = models.OneToOneField(User)
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'pk': self.pk})


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
        return reverse('entry_detail', kwargs={'pk':self.pk})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Entry, self).save(*args, **kwargs)


from guardian.shortcuts import assign_perm
from django.db.models.signals import post_save
def create_blog_permissions(sender, instance, created, **kwargs):
    if created:
        from django.contrib.auth.models import Group
        admins = Group.objects.get(name='admins')
        mods = Group.objects.get(name='mods')
        assign_perm('change_blog', instance.user, instance)
        assign_perm('delete_blog', instance.user, instance)
        assign_perm('change_blog', admins, instance)
        assign_perm('delete_blog', admins, instance)
        assign_perm('change_blog', mods, instance)
        assign_perm('delete_blog', mods, instance)

def create_entry_permissions(sender, instance, created, **kwargs):
    if created:
        from django.contrib.auth.models import Group
        admins = Group.objects.get(name='admins')
        mods = Group.objects.get(name='mods')
        assign_perm('change_entry', instance.blog.user, instance)
        assign_perm('delete_entry', instance.blog.user, instance)
        assign_perm('change_entry', admins, instance)
        assign_perm('delete_entry', admins, instance)
        assign_perm('change_entry', mods, instance)
        assign_perm('delete_entry', mods, instance)

post_save.connect(create_entry_permissions, sender=Entry)
post_save.connect(create_blog_permissions, sender=Blog)
