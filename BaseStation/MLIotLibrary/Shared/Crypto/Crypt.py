from Crypto.Cipher import AES
from Crypto import Random
from ..Schema import Node, SecurityProfile

class CryptoManager:


    def encrypt_message(self, message, recipentId):
        iv=Random.get_random_bytes(16)
        parent = Node.get_node_by_address(recipentId)
        profile=SecurityProfile.get_security_profile_by_parent_id(parent.id)
        key=profile.MessageKeys[profile.MessageIndex]
        cryptObj = AES.new(key, AES.MODE_CBC, iv)
        cipherinfo= [cryptObj.encrypt(message),iv]

        return cipherinfo

    def decrypt_message(self, message, iv, **kwargs):
        if 'senderAddress' in kwargs:
            parent = Node.get_node_by_address(kwargs.get('senderAddress'))
            profile = SecurityProfile.get_security_profile_by_parent_id(parent.id)
        elif 'profile' in kwargs:
            profile = kwargs.get('profile')
        else:
            raise ValueError('decrypt_message(): senderAddress or profile is null')
        key = profile.MessageKeys[profile.MessageIndex]
        crypt_obj = AES.new(key, AES.MODE_CBC, iv)
        plaintext = crypt_obj.decrypt(message)

        return plaintext

