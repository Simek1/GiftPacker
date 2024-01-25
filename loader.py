import os
import sys
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from base64 import urlsafe_b64decode

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
        settings=settings.splitlines()
        if len(settings)>8:
            try:
                self.rew_msg=settings[0]
                self.game_code=settings[1]
                self.mys1_msg=settings[2]
                self.mys1_code=settings[3]
                self.mys2_msg=settings[4]
                self.mys2_code=settings[5]
                self.safe_code=settings[6]
                self.quiz_code=settings[7]
                self.quiz_msg=settings[8]
                self.questions_num=int(settings[9])
                self.questions=[]
                self.answers=[]
                for i in range(10,10+self.questions_num*5, 5):
                    answers=[]
                    self.questions.append(settings[i])
                    answers.append(settings[i+1])
                    answers.append(settings[i+2])
                    answers.append(settings[i+3])
                    answers.append(settings[i+4])
                    self.answers.append(answers)
            except:
                print("Corupted settings file")
                return None
        else:
            print("Corrupted settings file")
            return None

if __name__ == "__main__":
    setts=Settings()
    for ar in dir(setts):
        print(ar, getattr(setts, ar))
    sys.exit()
