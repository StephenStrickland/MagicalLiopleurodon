from MLIotLibrary.Shared.Schema.Audit import Audit
from mongoengine import Document, StringField, BooleanField, ObjectIdField, IntField, ListField, EmbeddedDocumentField
__author__ = 'Stephen'


class MSecurityProfile(Document):
        meta = {'collection': 'SecurityProfiles'}
        Audit = EmbeddedDocumentField(Audit)
        ParentId = ObjectIdField(required=True)
        ParentType = IntField(required=True)
        NetworkEncryptionMethod = IntField(required=True, default=1)
        MessageEncryptionMethod = IntField(required=True, default=0)
        NetworkKeys = ListField(StringField())
        NetworkIndex = IntField(required=True, default=0)
        MessageKeys = ListField(StringField())
        MessageIndex = IntField(required=True, default=0)
        PreviousMessageIndex = IntField(required=True, default=0)
        PreviousNetworkIndex = IntField(required=True, default=0)
        PublicKey = StringField(required=False)
        PrivateKey = StringField(required=False)
        RSAEnabled = BooleanField(required=False, default=False)
        CurrentNonce = IntField(required=False, default=0)


def get_security_profile_by_parent_id(id):
    return MSecurityProfile.objects(ParentId=id).first()


def get_config(sec_profile):
        return {
                'i': sec_profile.id,
                'p': '',
                'nk': [x for x in sec_profile.NetworkKeys],
                'ni': sec_profile.NetworkIndex,
                'mk': [x for x in sec_profile.MessageKeys],
                'mi': sec_profile.MessageIndex,
                'np': sec_profile.PreviousNetworkIndex,
                'mp': sec_profile.PreviousMessageIndex,
                'n': sec_profile.CurrentNonce}


def create_security_profile(sec_profile):
        p = MSecurityProfile(**sec_profile)
        p.Audit = Audit()
        p.save()
        return p.id
