from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

class Message:
    def __init__(self, dataIv, dataString, dataSignedHash, senderId, nonce):
        self.iv=dataIv
        self.data=dataString
        self.signature=dataSignedHash
        self.sender=senderId
        self.nonce=nonce

    def validate(self):
        return True

    def getDict(self):
        return {
            'i': self.iv,
            'd': self.data,
            'sg': self.signature,
            's': self.sender,
            'n': self.nonce

        }
        


