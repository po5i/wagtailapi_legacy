from __future__ import absolute_import, unicode_literals

from django.conf.urls import include, url

from wagtailapi_legacy.v1 import urls as wagtailapi_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls


urlpatterns = [
    url(r'^api/', include(wagtailapi_urls)),

    url(r'^documents/', include(wagtaildocs_urls)),
    url(r'', include(wagtail_urls)),
]
