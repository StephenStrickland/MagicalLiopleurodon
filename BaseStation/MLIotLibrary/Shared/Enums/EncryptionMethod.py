from enum import Enum

__author__ = 'Stephen'


class EncryptionMethod(Enum):
    NONE = 0
    AES128 = 1
    AES256 = 2
    RSA = 3
