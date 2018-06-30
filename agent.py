"""An agent that can send and receive messages."""
import rsa as crypto

class Agent:

    def __init__(self, c=None):
        self.c = c if c else crypto.RSA(8)

    def encrypt_message(self, m, public_key):
        return self.c.encrypt(m, public_key)

    def decrypt_message(self, m):
        return self.c.decrypt(m)

    def get_public_key(self):
        return self.c.get_public_key()