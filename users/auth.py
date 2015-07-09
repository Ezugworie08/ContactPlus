__author__ = 'Chris:foresmac@vokal.io'

from django.contrib.auth import get_user_model
from rest_framework.authentication import BaseAuthentication


class TokenAuthentication(BaseAuthentication):
    # See documentation here: http://www.django-rest-framework.org/api-guide/authentication/#custom-authentication

    def authenticate(self, request):
        token = request.META.get('HTTP_AUTHORIZATION')

        if not token:
            return None

        # The value for the header should be something like: 'Token: e3f4c35c-7681-4b4c-aa8b-e63fb5c27a8d'
        # This line extracts the token from the value of the header
        token = token.split(':')[-1].strip()

        user_model = get_user_model()

        try:
            user = user_model.objects.get(token=token)
        except user_model.DoesNotExist:
            return None

        return user, None
