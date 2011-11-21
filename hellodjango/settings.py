# Django settings for hellodjango project.

import json
with open('/home/dotcloud/environment.json') as f:
  env = json.load(f)

import os
PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE':  'django.db.backends.postgresql_psycopg2',
        'NAME':    'template1',
        'USER':     env['DOTCLOUD_DB_SQL_LOGIN'],
        'PASSWORD': env['DOTCLOUD_DB_SQL_PASSWORD'],
        'HOST':     env['DOTCLOUD_DB_SQL_HOST'],
        'PORT':     int(env['DOTCLOUD_DB_SQL_PORT']),
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
#         'NAME': 'mydb',                       # Or path to database file if using sqlite3.
#         'USER': 'root',                       # Not used with sqlite3.
#         'PASSWORD': 'MySQLpassword',          # Not used with sqlite3.
#         'HOST': '',                           # Set to empty string for localhost. Not used with sqlite3.
#         'PORT': '',                           # Set to empty string for default. Not used with sqlite3.
#     }
# }

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = '/home/dotcloud/data/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
# STATIC_ROOT shouldn't contain anything that isn't generated by collectstatic.
STATIC_ROOT = '/home/dotcloud/data/static/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    PROJECT_PATH + '/static/',
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '!_1l5t^g34$58bl&eh))tz%&)tq$&(x_2d&0@zz7fh8=z^t%d#'

# List of callables that know how to import templates from various sources.
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
)

ROOT_URLCONF = 'hellodjango.urls'

TEMPLATE_DIRS = (
    PROJECT_PATH + '/templates/',
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles', 
    'django.contrib.admin',
    'django.contrib.admindocs',
    'forum',
    'django.contrib.markup',
#   'django_bcrypt',
    'userena', 'guardian', 'easy_thumbnails',
)

# Extension of the User model with forum-related fields in models.py
AUTH_PROFILE_MODULE = 'forum.UserProfile'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
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

### Only for production:
EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'
### http://sontek.net/using-gmail-to-send-e-mails-from-django
# EMAIL_HOST =           'smtp.gmail.com'
# EMAIL_HOST_USER =      '<example@gmail.com>'
# EMAIL_HOST_PASSWORD =  '<mypassword>'
# EMAIL_PORT =           587
# EMAIL_USE_TLS =        True
# EMAIL_SUBJECT_PREFIX = '[Pony Forum] '

### USERENA APP
ANONYMOUS_USER_ID = -1.

AUTHENTICATION_BACKENDS = (
    'userena.backends.UserenaAuthenticationBackend',
    'guardian.backends.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
)

LOGIN_REDIRECT_URL = '/'
LOGIN_URL          = '/accounts/login/'
LOGOUT_URL         = '/accounts/logout/'

USERENA_ACTIVATION_REQUIRED  = True # Set to false when debugging
USERENA_DEFAULT_PRIVACY      = 'open'
USERENA_DISABLE_PROFILE_LIST = True
USERENA_FORBIDDEN_USERNAMES  = ('activate', 'login', 'logout', 'me',\
                                'password', 'register', 'signin',\
                                'signout', 'signup')
USERENA_MUGSHOT_GRAVATAR     = False
USERENA_USE_HTTPS            = True
###

### BCRYPT APP, if used
BCRYPT_MIGRATE = True
BCRYPT_ROUNDS  = 16
###