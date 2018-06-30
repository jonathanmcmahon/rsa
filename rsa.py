"""An RSA cryptosystem engine."""
import randomprime as rp
import helpers as util


class RSA:

    prime_gen = rp.RandomPrimeGenerator()

    def __init__(self, bits, verbose=False, p=None, q=None, e=None):
        self.verbose = verbose
        self.p = p if p else self.prime_gen.generate(bits) # TOP SECRET!!!
        self.q = q if q else self.prime_gen.generate(bits) # TOP SECRET!!!
        self.e = e if e else self._generate_public_key()
        self.d = self._generate_private_key()
        if self.verbose:
            print("p: %d, q: %d, e: %d, d: %d" % (self.p, self.q, self.e, self.d))

    def _get_n(self):
        return self.p * self.q

    def _generate_public_key(self):
        """Create the public key."""
        p, q = self.p, self.q
        for i in range(3, (p * q) / 2):
            if util.relatively_prime(i, (p - 1) * (q - 1)):
                return i
        raise Exception("Could not find a public key relatively prime to (p-1)(q-1)!")

    def _generate_private_key(self):
        """Create the private key."""
        p, q, e = self.p, self.q, self.e
        x, y, d = util.extended_euclid(e, (p - 1) * (q - 1))
        assert d == 1
        assert (x * e) % ((p-1)*(q-1)) == 1
        return x if x >= 0 else x + ((p-1)*(q-1))

    def get_public_key(self):
        """Return the current cryptosystem's public key."""
        return tuple((self._get_n(), self.e))

    def encrypt(self, msg, public_key):
        """Encrypt a message using any public key."""
        n, e = public_key
        return (msg ** e) % n

    def decrypt(self, msg, private_key=None):
        n = self._get_n()
        if not private_key:
            private_key = self.d
        return (msg ** private_key) % n
