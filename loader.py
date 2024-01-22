import os
import sys
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from base64 import urlsafe_b64encode, urlsafe_b64decode

class Settings(object):
    def __init__(self):
        if os.path.exists("conf/key.key") and os.path.exists("conf/settings.bin"):
            with open("conf/key.key", "rb") as key_file:
                key=key_file.read()
            with open("conf/settings.bin", "rb") as settings_file:
                ciphered_settings=settings_file.read()
            cipher=Cipher(algorithms.AES(key[:32]), modes.CFB8(key[32:]), backend=default_backend())
            decryptor=cipher.decryptor()
            settings=decryptor.update(urlsafe_b64decode(ciphered_settings)) + decryptor.finalize()
            settings=settings.decode(errors="ignore")
            print(settings)
        settings=settings.splitlines
        if len(settings)>8:
            pass
        else:
            return 0
            print("Corrupted settings file")

if __name__ == "__main__":
    Settings()
    sys.exit()
