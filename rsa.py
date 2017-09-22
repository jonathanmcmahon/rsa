"""An RSA cryptosystem engine."""
import randomprime as rp
import helpers as util


class RSA:

    prime_gen = rp.RandomPrimeGenerator()

    def __init__(self, bits):
        self.p = self.prime_gen(bits) # TOP SECRET!!!
        self.q = self.prime_gen(bits) # TOP SECRET!!!
        self.e = self._generate_public_key()
        self.d = self._generate_private_key()

    def _get_n(self):
        return self.p * self.q

    def get_public_key(self):
        return tuple((self._get_n, self.e))

    def _generate_public_key(self):
        p, q = self.p, self.q
        for i in range(3, (p * q) / 2):
            if util.relatively_prime(i, (p - 1) * ( q - 1)):
                return i
        raise "Could not find a public key relatively prime to (p-1)(q-1)!"

    def _generate_private_key(self):
        p, q, e = self.p, self.q, self.e
        x, y, d = util.extended_euclid(e, (p - 1) * (q - 1))
        assert d == 1
        return x