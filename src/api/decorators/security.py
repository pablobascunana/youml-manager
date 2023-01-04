from rest_framework import status
from rest_framework.response import Response

from api.services.jwt import JwtToken

AUTHORIZATION_KEY = 'Authorization'


def token_required(view_function):
    def wrapper(request, *args, **kwargs):
        if AUTHORIZATION_KEY in request.headers:
            if payload := JwtToken().decode(request.headers[AUTHORIZATION_KEY]):
                kwargs['payload'] = payload
                return view_function(request, *args, **kwargs)
        return Response(status=status.HTTP_403_FORBIDDEN)
    return wrapper
