import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
     ('Karambir Singh Nain', 'karambir@codesters.org'),
     ('Mohammad Adil', 'adil@codesters.org'),
     ('Mayank Jain', 'mayank@codesters.org'),
)

MANAGERS = ADMINS

DJANGO_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.sitemaps',
)

THIRD_PARTY_APPS = (
    'south',
    'django_extensions',
    'registration',
    'guardian',
    'widget_tweaks',
    'braces',
    'djangoratings',
    'disqus',
)

LOCAL_APPS = (
    'profiles',
#    'tracks',
    'resources',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

MEDIA_URL = '/media/'

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'assets')

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)

AUTHENTICATION_BACKENDS = (
        'django.contrib.auth.backends.ModelBackend',
        'guardian.backends.ObjectPermissionBackend',
)

ALLOWED_HOSTS = []
TIME_ZONE = 'Asia/Kolkata'

LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = False
USE_L10N = True
USE_TZ = False

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

SECRET_KEY = '(r2el3qxdzm1&amp;)mxyllv56%8)r1$c*uvc1&amp;8x4mn*et#z)hj0)'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    #'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.static',
)


ROOT_URLCONF = 'codesters.urls'

WSGI_APPLICATION = 'codesters.wsgi.application'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

#DJANGO extended settings we are using
LOGIN_REDIRECT_URL = '/resource/'
ABSOLUTE_URL_OVERRIDES = {
        'auth.user': lambda u: "/profile/%s/" % u.username,
}

#Django-Registration Settings
ACCOUNT_ACTIVATION_DAYS = 7


#Django-Guardian Settings
ANONYMOUS_USER_ID = -1
GUARDIAN_RENDER_403 = True

#Django-Ratings Settings
RATINGS_VOTES_PER_IP = 20

#Disqus Settings
DISQUS_API_KEY = 'lTuOXBAfTK3symHWvi7cZHgcYipkL32BoSud7f0H4gl4lfVhVw0HCcbcmiu1rWJY'
DISQUS_WEBSITE_SHORTNAME = 'codesters'

#Import Local and Prod settings
try:
    from local_settings import *
except ImportError:
    pass

try:
    from prod_settings import *
except ImportError:
    pass
