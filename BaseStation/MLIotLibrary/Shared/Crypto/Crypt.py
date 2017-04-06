from Crypto.Cipher import AES
from Crypto import Random
from ..Schema import Node, SecurityProfile

class CryptoManager:

    def __init__(self, securityProfile):
        self.profile=securityProfile

    def encryptMessage(self, message, recipentId):
        iv=Random.get_random_bytes(16)
        parent = Node.get_node_by_address(recipentId)
        profile=SecurityProfile.get_security_profile_by_parent_id(parent.id)
        key=profile.MessageKeys[profile.MessageIndex]
        cryptObj = AES.new(key, AES.MODE_CBC, iv)
        cipherinfo= [cryptObj.encrypt(message),iv]

        return cipherinfo

    def decryptMessage(self, message, iv, senderId):
        parent = Node.get_node_by_address(senderId)
        profile = SecurityProfile.get_security_profile_by_parent_id(parent.id)
        key = profile.MessageKeys[profile.MessageIndex]
        cryptObj = AES.new(key, AES.MODE_CBC, iv)
        plaintext = cryptObj.decrypt(message)
        return plaintext

