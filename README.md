# wagtailapi_legacy

This repository contains implementations of versions of the Wagtail API that are no longer maintained by the core team.
This is to allow older projects to still use an unsupported version of the API on newer versions of Wagtail.

**Please note:** While the intention of this repository is to keep old versions of the API working on the latest version of
Wagtail, the Wagtail core team are not committed to carrying out much of this work. If it doesn't work with the version of
Wagtail you are using, please fork it and make any required changes yourself in your own fork rather than opening an issue
(pull requests are welcome).

## Installation

Install from pip:

    pip install wagtailapi_legacy

### V1

The V1 API was removed in Wagtail 2.0. To keep using it in newer versions, replace all occurances of ``wagtail.contrib.wagtailapi`` with ``wagtailapi_legacy.v1``.
