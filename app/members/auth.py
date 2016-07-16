from django.contrib.auth.models import AnonymousUser
from django.conf import settings

from rest_framework import authentication
from rest_framework import permissions
from rest_framework import exceptions

import logging
LOG = logging.getLogger(__name__)



class StaticTokenAuth(authentication.BaseAuthentication):
   """
   Allows API access using a predetermined static token.
   This is mainly used when horizon or other external
   services needs to talk to the API when the user is not authenticated.

   It limits possibility of someone playing with the API from a
   location they should not be doing so...
   """
   def authenticate(self, request):
       token = request.META.get('HTTP_X_AUTH_TOKEN', None)
       LOG.debug("HTTP_X_AUTH_TOKEN : " + str(token))
       if token:
           if token == settings.STATIC_API_TOKEN:
               return (None, None)
           else:
               raise exceptions.AuthenticationFailed('Authentication Failed')
       else:
           raise exceptions.AuthenticationFailed('No token provided')
