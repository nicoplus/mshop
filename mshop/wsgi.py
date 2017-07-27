"""
WSGI config for mshop project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from dj_static import Cling

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mblog.settings")

application = Cling(get_wsgi_application())



# +++++++++++ DJANGO +++++++++++
# To use your own django app use code like this:
#import os
#import sys
#
## assuming your django settings file is at '/home/nicoplus/mysite/mysite/settings.py'
## and your manage.py is is at '/home/nicoplus/mysite/manage.py'
#path = '/home/nicoplus/mysite'
#if path not in sys.path:
#    sys.path.append(path)
#
#os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
#
## then, for django >=1.5:
#from django.core.wsgi import get_wsgi_application
#application = get_wsgi_application()
## or, for older django <=1.4
#import django.core.handlers.wsgi
#application = django.core.handlers.wsgi.WSGIHandler()