import os


PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))
DEBUG = False
LOCAL_DEVELOPMENT = True
DOTCLOUD_ENVIRONMENT, TRAVIS_ENVIRONMENT = False, False

if 'DOTCLOUD_ENVIRONMENT' in os.environ:
    import json

    with open('/home/dotcloud/environment.json') as f:
        env = json.load(f)
    LOCAL_DEVELOPMENT = False
    DOTCLOUD_ENVIRONMENT = True
elif 'TRAVIS' in os.environ:
    LOCAL_DEVELOPMENT = False
    TRAVIS_ENVIRONMENT = True

#ADMINS = (
#    try:
#        # ('Your Name', 'your_email@example.com'),
#        (env['ADMIN_NAME'], env['ADMIN_EMAIL']),
#    except NameError, KeyError:
#        pass
#)
#
#MANAGERS = ADMINS

if DOTCLOUD_ENVIRONMENT:
    # Do not alter these values under normal circumstances:
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
elif TRAVIS_ENVIRONMENT:
    DATABASES = {
        'default': {
            'ENGINE':   'django.db.backends.postgresql_psycopg2',
            'NAME':     'travisdb',  # Must match travis.yml setting
            'USER':     'postgres',
            'PASSWORD': '',
            'HOST':     'localhost',
            'PORT':     '',
        }
    }

### Enter your local database information in local_settings.py
### An example_local_settings.py exists to give you an idea of
### how to set it up

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
if not LOCAL_DEVELOPMENT:
    TIME_ZONE = env.get('TIME_ZONE', 'America/Chicago')
else:
    TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
if not LOCAL_DEVELOPMENT:
    LANGUAGE_CODE = env.get('LANGUAGE_CODE', 'en-us')
else:
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
if DOTCLOUD_ENVIRONMENT:
    MEDIA_ROOT = '/home/dotcloud/data/media/'
else:
    MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
# STATIC_ROOT shouldn't contain anything that isn't generated by collectstatic.
if DOTCLOUD_ENVIRONMENT:
    STATIC_ROOT = '/home/dotcloud/data/static/'
else:
    STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

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
try:
    SECRET_KEY
except NameError:
    SECRET_FILE = os.path.join(PROJECT_PATH, 'secret.txt')
    try:
        SECRET_KEY = open(SECRET_FILE).read().strip()
    except IOError:
        try:
            import random
            SECRET_KEY = ''.join([random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])
            secret = file(SECRET_FILE, 'w')
            secret.write(SECRET_KEY)
            secret.close()
        except IOError:
            Exception('Please create a %s file with random characters \
            to generate your secret key!' % SECRET_FILE)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#   'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'djangosecure.middleware.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'ponyforum.urls'

TEMPLATE_DIRS = (
    PROJECT_PATH + '/templates/',
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'forum',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.markup',
    'django.contrib.humanize',
    'registration',
#   'cache_panel',
    'south',
    'django_nose',
    'djangosecure',
)

# Extension of the User model with forum-related fields in models.py
AUTH_PROFILE_MODULE = 'forum.UserProfile'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
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

### PONY-FORUM APP
if LOCAL_DEVELOPMENT:
    POSTS_PER_PAGE         = 25
    THREADS_PER_PAGE       = 25
    USER_POSTS_PER_PAGE    = 10
    USER_THREADS_PER_PAGE  = 25
    SUBSCRIPTIONS_PER_PAGE = 25
    BOOKMARKS_PER_PAGE     = 35
    SAVES_PER_PAGE         = 10
else:
    POSTS_PER_PAGE         = int(env.get('POSTS_PER_PAGE', '25'))
    THREADS_PER_PAGE       = int(env.get('THREADS_PER_PAGE', '25'))
    USER_POSTS_PER_PAGE    = int(env.get('USER_POSTS_PER_PAGE', '10'))
    USER_THREADS_PER_PAGE  = int(env.get('USER_THREADS_PER_PAGE', '25'))
    SUBSCRIPTIONS_PER_PAGE = int(env.get('SUBSCRIPTIONS_PER_PAGE', '25'))
    BOOKMARKS_PER_PAGE     = int(env.get('BOOKMARKS_PER_PAGE', '35'))
    SAVES_PER_PAGE         = int(env.get('SAVES_PER_PAGE', '10'))

# If you change these default values without changing the URLs style.css,
# the icons will break, because their URLs are hardcoded.
#
# You will have to change them in the CSS manually for now.
LOGIN_REDIRECT_URL     = '/'
LOGIN_URL              = '/accounts/login/'
LOGOUT_URL             = '/accounts/logout/'
REGISTRATION_URL       = '/accounts/register/'
SITE_CONFIGURATION_URL = '/configuration/'
###

### E-MAIL SERVER
## http://sontek.net/using-gmail-to-send-e-mails-from-django
if not LOCAL_DEVELOPMENT:
    EMAIL_HOST          = env.get('EMAIL_HOST', 'smtp.gmail.com')
    EMAIL_HOST_USER     = env.get('EMAIL_HOST_USER', 'myusername@gmail.com')
    EMAIL_HOST_PASSWORD = env.get('EMAIL_HOST_PASSWORD', 'mypassword')
    EMAIL_PORT          = int(env.get('EMAIL_PORT', '587'))
    EMAIL_USE_TLS       = env.get('EMAIL_USE_TLS', 'True') == 'True'
    DEFAULT_FROM_EMAIL  = env.get('DEFAULT_FROM_EMAIL',
                                  'noreply@equestria.pony')
#    EMAIL_SUBJECT_PREFIX = ""  # Doesn't work, optional
###

### DJANGO-REGISTRATION
if LOCAL_DEVELOPMENT:
    ACCOUNT_ACTIVATION_DAYS = 7
    REGISTRATION_OPEN = True
else:
    ACCOUNT_ACTIVATION_DAYS = int(env.get('ACCOUNT_ACTIVATION_DAYS', '7'))
    REGISTRATION_OPEN = env.get('REGISTRATION_OPEN', 'True') == 'True'
###

### DJANGO-SECURE HTTPS
if not LOCAL_DEVELOPMENT:
    SECURE_FRAME_DENY = True
    SECURE_HSTS_SECONDS = 1
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_BROWSER_XSS_FILTER = True
    # SECURE_SSL_REDIRECT = True
        # Disable for dotCloud: http://tinyurl.com/conn569
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
###

### Secure Django (Native Features)
    # SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTOCOL", "https")
        # Disable for dotCloud
###

### DJANGO-NOSE
NOSE_ARGS = [
    '--with-fixture-bundling',
    '--with-coverage',
    '--cover-tests',
    '--cover-package=\
forum.model_tests,\
forum.view_tests,\
forum.form_tests,\
forum.input_tests,\
forum.installed_apps_order_tests'
]

NOSE_PLUGINS = [
    'nose.plugins.cover.Coverage'
]

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
###

try:
    LOCAL_SETTINGS
except NameError:
    try:
        from local_settings import *
    except ImportError:
        pass

### DJANGO-DEBUG-TOOLBAR
if DEBUG:
    INSTALLED_APPS += ('debug_toolbar',)
    MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
    if LOCAL_DEVELOPMENT:
        INTERNAL_IPS = ('127.0.0.1',)
###
