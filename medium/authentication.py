import re

from django.conf import settings
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from django.http import HttpResponse

def validate_authorization_token(token):
    """
    """
    try:
        session = Session.objects.get(session_key=token)
        session_data = session.get_decoded()
        uid = session_data.get('_auth_user_id')
        user = User.objects.get(id=uid)
        return user, False
    except:
        return None, True

class AuthTokenMiddleware(object):
    """
        Authentication Middleware for logging in with an auth token.
        Backend will get user.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if 'HTTP_AUTHORIZATION' not in request.META:
            return self.get_response(request)
        token = None
        auth_header = request.META['HTTP_AUTHORIZATION']
        auth_method, token = re.split(re.compile(r'\s+', re.U), auth_header, 1)

        if auth_method != 'Bearer':
            return HttpResponse('Authorization header should be in the format "Bearer token"', status=400)
        if token is None:
            return
        user = None
        user, err = validate_authorization_token(token)
        if user is None:
            return self.get_response(request)
        request.user = user
        return self.get_response(request)
