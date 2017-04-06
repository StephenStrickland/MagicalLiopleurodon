from MLIotLibrary.Shared.Schema.Audit import Audit
from mongoengine import Document, DateTimeField, StringField, EmbeddedDocumentField, BooleanField, IntField


class MUser(Document):
    Audit = EmbeddedDocumentField(Audit)
    FirstName = StringField()
    LastName = StringField()
    UserName = StringField(required=True)
    Password = StringField(required=True)
    PasswordSalt = StringField(required=True)
    AuthToken = StringField(required=True)
    AuthTokenExpiration = DateTimeField(required=True)
    IsBot = BooleanField(required=True)


def get_user_by_id(id):
    return MUser.objects(id=id).first()


def get_users_by_username(name):
    return MUser.objects(UserName=name)


def get_users():
    return MUser.objects()


def get_user_bots():
    return MUser.objects(IsBot=True)

