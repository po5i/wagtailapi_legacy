from __future__ import absolute_import, unicode_literals

from django.conf.urls import include, url

from wagtailapi_legacy_v1 import urls as wagtailapi_urls
from wagtail.wagtailcore import urls as wagtail_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls


urlpatterns = [
    url(r'^api/', include(wagtailapi_urls)),

    url(r'^documents/', include(wagtaildocs_urls)),
    url(r'', include(wagtail_urls)),
]
