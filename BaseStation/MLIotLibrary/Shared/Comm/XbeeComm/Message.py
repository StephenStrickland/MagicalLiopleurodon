from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
import json
from ....Shared.Crypto import Crypt

class Message:
    def __init__(self, dataIv, dataString, dataSignedHash, senderId, recipientList, nonce):
        self.iv=dataIv
        self.data={"dataString":dataString, "nonce":nonce}
        self.encData = ""
        self.signature=dataSignedHash
        self.sender=senderId
        self.recipients=recipientList

    def validate(self):
        return True

    def getDict(self):
        return {
            'i': self.iv,
            'd': self.encData,
            'sg': self.signature,
            's': self.sender,
            'r': self.recipients

        }
    def prepMessage(self, recipient):
        self.encData=Crypt.CryptoManager.encryptMessage(json.dumps(self.data),recipient)

    def processMessage(self):
        self.data=json.loads(Crypt.CryptoManager.decryptMessage(self.encData,self.iv,self.sender))

        


