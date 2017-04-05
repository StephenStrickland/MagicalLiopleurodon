from MLIotLibrary.Shared.Schema.Audit import Audit
from mongoengine import Document, DateTimeField, StringField, EmbeddedDocumentField, BooleanField, IntField

class User(Document):
    Audit = EmbeddedDocumentField(Audit)
    FirstName = StringField()
    LastName = StringField()
    UserName = StringField(required=True)
    Password = StringField(required=True)
    PasswordSalt = StringField(required=True)
    AuthToken = StringField(required=True)
    AuthTokenExpiration = DateTimeField(required=True)
    IsBot = BooleanField(required=True)
