__author__ = 'Stephen'


class IUserRepo:
    def get_user_by_id(self, id):
        return NotImplementedError()
    def get_user_by_username(self, username):
        return NotImplementedError()
    def get_user_by_auth_token(self, token):
        return NotImplementedError()