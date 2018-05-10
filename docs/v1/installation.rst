Wagtail API Installation
========================


To install, add ``wagtailapi_legacy`` and ``rest_framework`` to ``INSTALLED_APPS`` in your Django settings and configure a URL for it in ``urls.py``:

.. code-block:: python

    # settings.py

    INSTALLED_APPS = [
        ...
        'wagtailapi_legacy',
        'rest_framework',
    ]

    # urls.py

    from wagtailapi_legacy.v1 import urls as wagtailapi_urls

    urlpatterns = [
        ...

        url(r'^api/', include(wagtailapi_urls)),

        ...

        # Ensure that the wagtailapi_urls line appears above the default Wagtail page serving route
        url(r'', include(wagtail_urls)),
    ]
