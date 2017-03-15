__author__ = 'Stephen Strickland'
from functools import wraps
from bottle import request, response, HTTPError
import configparser
from MLIotLibrary.Shared.Respositories.UserMongoRepository import UserMongoRepository
from datetime import datetime
import hashlib


class AuthService:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('lio.config')
        self.db = UserMongoRepository()

    def is_valid_auth_token(self, token):
        user = self.db.get_user_by_auth_token(token)
        if user and user.AuthTokenExpiration >= datetime.utcnow():
            return True
        return False

    def validate_username_password(self, username, password):
        user = self.db.get_user_by_username(username)
        if user and hashlib.sha512(user.PasswordSalt + password).hexdigest() == user.Password:
            return True
        return False


def authentication_wrapper(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = request.get_header('Authorization')
        if not token or not AuthService().is_valid_auth_token(token):
            err = HTTPError(401, 'Not Authorized')
            err.add_header('WWW-Authenticate', 'Basic token')
            return err
        return f(*args, **kwargs)
    return wrapper
