from __future__ import absolute_import, unicode_literals

import os

import django

DEBUG = False

MEDIA_URL = '/media/'

TIME_ZONE = 'Asia/Tokyo'

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DATABASE_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': os.environ.get('DATABASE_NAME', 'wagtail'),
        'USER': os.environ.get('DATABASE_USER', None),
        'PASSWORD': os.environ.get('DATABASE_PASS', None),
        'HOST': os.environ.get('DATABASE_HOST', None),

        'TEST': {
            'NAME': os.environ.get('DATABASE_NAME', None),
        }
    }
}

# Add extra options when mssql is used (on for example appveyor)
if DATABASES['default']['ENGINE'] == 'sql_server.pyodbc':
    DATABASES['default']['OPTIONS'] = {
        'driver': 'SQL Server Native Client 11.0',
        'MARS_Connection': 'True',
    }


# explicitly set charset / collation to utf8 on mysql
if DATABASES['default']['ENGINE'] == 'django.db.backends.mysql':
    DATABASES['default']['TEST']['CHARSET'] = 'utf8'
    DATABASES['default']['TEST']['COLLATION'] = 'utf8_general_ci'


SECRET_KEY = 'not needed'

ROOT_URLCONF = 'tests.urls'

USE_TZ = True

MIDDLEWARE = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'wagtail.wagtailcore.middleware.SiteMiddleware',
    'wagtail.wagtailredirects.middleware.RedirectMiddleware',
)

INSTALLED_APPS = (
    'wagtailapi_legacy_v1',

    # Install wagtailredirects with its appconfig
    # Theres nothing special about wagtailredirects, we just need to have one
    # app which uses AppConfigs to test that hooks load properly
    'wagtail.wagtailredirects.apps.WagtailRedirectsAppConfig',

    'wagtail.tests.testapp',
    'wagtail.tests.demosite',
    'wagtail.tests.customuser',
    'wagtail.wagtailforms',
    'wagtail.wagtailsearch',
    'wagtail.wagtailembeds',
    'wagtail.wagtailimages',
    'wagtail.wagtailsites',
    'wagtail.wagtailusers',
    'wagtail.wagtailsnippets',
    'wagtail.wagtaildocs',
    'wagtail.wagtailadmin',
    'wagtail.wagtailcore',

    'taggit',
    'rest_framework',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
)


# Using DatabaseCache to make sure that the cache is cleared between tests.
# This prevents false-positives in some wagtail core tests where we are
# changing the 'wagtail_root_paths' key which may cause future tests to fail.
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'cache',
    }
}

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',  # don't use the intentionally slow default password hasher
)


WAGTAILSEARCH_BACKENDS = {
    'default': {
        'BACKEND': 'wagtail.wagtailsearch.backends.db',
    }
}

AUTH_USER_MODEL = 'customuser.CustomUser'

WAGTAIL_SITE_NAME = "Test Site"

# Extra user field for custom user edit and create form tests. This setting
# needs to here because it is used at the module level of wagtailusers.forms
# when the module gets loaded. The decorator 'override_settings' does not work
# in this scenario.
WAGTAIL_USER_CUSTOM_FIELDS = ['country', 'attachment']

WAGTAILADMIN_RICH_TEXT_EDITORS = {
    'default': {
        'WIDGET': 'wagtail.wagtailadmin.rich_text.HalloRichTextArea'
    },
    'custom': {
        'WIDGET': 'wagtail.tests.testapp.rich_text.CustomRichTextArea'
    },
}
