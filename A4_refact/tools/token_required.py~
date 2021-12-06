import jwt

from functools import wraps
from flask import request, redirect, g
from flask_json import FlaskJSON, JsonError, json_response, as_json

from tools.logging import logger

from tools.get_aws_secrets import get_secrets


def token_required(f):
    @wraps(f)
    def _verify(*args, **kwargs):
        secrets = get_secrets()
        auth_headers = request.headers.get('Authorization', '').split(':')

        invalid_msg = {
            'message' : 'Invalid token. Registration and/or authentication required',
            'authenticated' : False
            }

        expired_msg = {
            'message' : 'Expired token. Reauthentication required.',
            'authenticated' : False
            }

        if len(auth_headers) != 2:
            return json_response(status_ = 401, message = invalid_msg)

    return _verify
