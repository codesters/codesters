import re
from django.template.defaultfilters import slugify


def unique_slugify(instance, value, slug_field_name='slug', queryset=None,
                   slug_separator='-'):
    """
    Calculates and stores a unique slug of ``value`` for an instance.

    ``slug_field_name`` should be a string matching the name of the field to
    store the slug in (and the field to check against for uniqueness).

    ``queryset`` usually doesn't need to be explicitly provided - it'll default
    to using the ``.all()`` queryset from the model's default manager.
    """
    slug_field = instance._meta.get_field(slug_field_name)

    slug = getattr(instance, slug_field.attname)
    slug_len = slug_field.max_length

    # Sort out the initial slug, limiting its length if necessary.
    slug = slugify(value)
    if slug_len:
        slug = slug[:slug_len]
    slug = _slug_strip(slug, slug_separator)
    original_slug = slug

    # Create the queryset if one wasn't explicitly provided and exclude the
    # current instance from the queryset.
    if queryset is None:
        queryset = instance.__class__._default_manager.all()
    if instance.pk:
        queryset = queryset.exclude(pk=instance.pk)

    # Find a unique slug. If one matches, at '-2' to the end and try again
    # (then '-3', etc).
    next = 2
    while not slug or queryset.filter(**{slug_field_name: slug}):
        slug = original_slug
        end = '%s%s' % (slug_separator, next)
        if slug_len and len(slug) + len(end) > slug_len:
            slug = slug[:slug_len-len(end)]
            slug = _slug_strip(slug, slug_separator)
        slug = '%s%s' % (slug, end)
        next += 1

    setattr(instance, slug_field.attname, slug)


def _slug_strip(value, separator='-'):
    """
    Cleans up a slug by removing slug separator characters that occur at the
    beginning or end of a slug.

    If an alternate separator is used, it will also replace any instances of
    the default '-' separator with the new separator.
    """
    separator = separator or ''
    if separator == '-' or not separator:
        re_sep = '-'
    else:
        re_sep = '(?:-|%s)' % re.escape(separator)
    # Remove multiple instances and if an alternate separator is provided,
    # replace the default '-' separator.
    if separator != re_sep:
        value = re.sub('%s+' % re_sep, separator, value)
    # Remove separator from the beginning and end of the slug.
    if separator:
        if separator != '-':
            re_sep = re.escape(separator)
        value = re.sub(r'^%s+|%s+$' % (re_sep, re_sep), '', value)
    return value


import requests, json, collections
highest = 0

# Used by get_initial_ratings
def total(a, d, f, g, r, t):
    """ Takes the total likes, +1's, ranks, etc from Alexa, Delicious, Facebook, Google+, Reddit, Twitter as arguments and returns total points according to their weight given below """
    global highest  # global variable for taking highest points
    a = 30000000 - a  # making alexa ranks in increasing order

    # weight of points for each domain in percentage
    alexa = 10
    facebook = 15
    googleplus = 25
    twitter = 25
    reddit = 15
    delicious = 10

    total = (facebook/100.0*f) + (googleplus/100.0*g) + (twitter/100.0*t) + (alexa/100.0*a) + (reddit/100.0*r) + (delicious/100.0*d)
    if total > highest:
        highest = total
    return total

# Used by get_initial_ratings
def ratings(points):
    """ Takes the total points of a url coming from total() as argument and returns the rating out of five """
    return int(points/highest*5)

# Used by get_initial_ratings
def convert(data):
    """ Takes unicode data as argument and returns string data """
    if isinstance(data, unicode):
        return str(data)
    elif isinstance(data, collections.Mapping):
        return dict(map(convert, data.iteritems()))
    elif isinstance(data, collections.Iterable):
        return type(data)(map(convert, data))
    else:
        return data

def get_initial_ratings(resource):
    """ Takes resource context as argument and returns its initial ratings using its likes, tweets, ranks, etc """

    url = resource.url
    alexa = convert(requests.get("http://api.camcimcumcem.com/alexa/rank/?domain=%s&output=json" %url).json())
    all_ranks = convert(requests.get("http://api.sharedcount.com/?url=%s" %url).json())

    # for making alexa rank with no data to be count as zero
    if alexa['rank'] == 'no data':
        alexa['rank'] = '30000000'

    vote = ratings(total(int(alexa['rank']), int(all_ranks['Delicious']), int(all_ranks['Facebook']['total_count']), int(all_ranks['GooglePlusOne']), int(all_ranks['Reddit']), int(all_ranks['Twitter'])))

    return
