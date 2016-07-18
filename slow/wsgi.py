"""
WSGI config for slow project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os, sys

"""sys.path.append('/directory/path/to/your/WebApp/location')
sys.path.append('/directory/path/to/your/WebApp/location/slow')"""
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "slow.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

