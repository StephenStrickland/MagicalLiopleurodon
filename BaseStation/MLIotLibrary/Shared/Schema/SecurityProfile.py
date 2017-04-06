from MLIotLibrary.Shared.Schema.Audit import Audit
from mongoengine import Document, StringField, BooleanField, ObjectIdField, IntField, ListField, EmbeddedDocumentField
__author__ = 'Stephen'


class MSecurityProfile(Document):
        Audit = EmbeddedDocumentField(Audit)
        ParentId = ObjectIdField(required=True)
        ParentType = IntField(required=True)
        NetworkEncryptionMethod = IntField(required=True, default=1)
        MessageEncryptionMethod = IntField(required=True, default=0)
        NetworkKeys = ListField(StringField())
        NetworkIndex = IntField(required=True, default=0)
        MessageKeys = ListField(StringField())
        MessageIndex = IntField(required=True, default=0)
        PublicKey = StringField(required=False)
        PrivateKey = StringField(required=False)
        RSAEnabled = BooleanField(required=False, default=False)
        CurrentNonce = IntField(required=False)


def get_security_profile_by_parent_id(id):
    return MSecurityProfile.objects(id=id).first()