from datetime import datetime, timedelta
from django.utils.timesince import timesince
from urlparse import urlparse
from django.core.urlresolvers import reverse
from django import template

from profiles.models import SavedResource, TopicFollow

register = template.Library()

@register.simple_tag
def check_active_button(path, word):
    word = '/' + word
    if word in path:
        return 'active'
    return ''

@register.simple_tag
def check_active(path, word):
    if word=='all':
        if '?' not in path:
            return 'active'
    word = '=' + word
    if word in path:
        return 'active'
    return ''

@register.simple_tag
def active(path, pattern):
    import re
    if re.search(pattern, path):
        return 'active'
    return ''

@register.filter
def age(value):
    now = datetime.now()
    try:
        difference = now - value
    except:
        return value
    if difference <= timedelta(minutes=1):
        return 'just now'
    return '%(time)s ago' % {'time': timesince(value).split(', ')[0]}

@register.filter
def domain(url):
    u = urlparse(url)
    return u[0] + '://' + u[1] + '/'

@register.filter
def website(url):
    u = urlparse(url)
    return u[1]

@register.filter
def isfollow(topic, user):
    try:
        TopicFollow.objects.get(topic=topic, user=user)
        return True
    except TopicFollow.DoesNotExist:
        return False

@register.filter
def issaved(resource, user):
    try:
        SavedResource.objects.get(resource=resource, user=user)
        return True
    except SavedResource.DoesNotExist:
        return False
