from datetime import datetime, timedelta
from django.utils.timesince import timesince
from urlparse import urlparse
from django.core.urlresolvers import reverse
from django import template

register = template.Library()

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
