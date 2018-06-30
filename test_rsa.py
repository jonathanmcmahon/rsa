"""Unit tests for RSA cryptosystem and related modules."""
import unittest
import agent
import helpers as util
import rsa as crypto
import randomprime as rp


class TestUtilFunctions(unittest.TestCase):

    def setUp(self):
        self.alice = agent.Agent()
        self.bob = agent.Agent()
        self.r = crypto.RSA(8, verbose=True)
        self.pg = rp.RandomPrimeGenerator()

    def test_relatively_prime(self):
        self.assertEqual(util.relatively_prime(12, 13), True)
        self.assertEqual(util.relatively_prime(12, 14), False)
        self.assertEqual(util.relatively_prime(20, 79), True)
        self.assertEqual(util.relatively_prime(3, 62), True)
        self.assertEqual(util.relatively_prime(5, 23), True)
        self.assertEqual(util.relatively_prime(21, 91), False)

    def test_extended_euclid(self):
        assert util.extended_euclid(20, 79) == (4.0, -1.0, 1)
        x, y, d = util.extended_euclid(3, 62)
        assert (3 * x) % 62 == 1
        x, y, d = util.extended_euclid(5, 23)
        assert (5 * x) % 23 == 1

    def test_mult_mod_inverse(self):
        assert util.mod_mult_inverse(20, 79) == 4.0
        assert util.mod_mult_inverse(3, 62) == 21.0
        assert util.mod_mult_inverse(5, 23) == 14.0
        assert util.mod_mult_inverse(21, 91) is None

    def test_generate_public_key(self):
        r = self.r
        r.p = 2
        r.q = 4
        with self.assertRaises(Exception):
            r._generate_public_key()

    def test_generate_private_key(self):
        r = self.r
        # d should be the inverse of e mod (p-1)(q-1)
        d_inverted = r.d * (r.e % ((r.p - 1) * (r.q - 1)))
        print("d inverted: %d" % d_inverted)
        assert d_inverted % ((r.p - 1) * (r.q - 1)) == 1

    def test_is_prime(self):
        with open('primes.txt') as f:
            list_primes = [map(int, line.split()) for line in f][0]
        for i in range(2,7920):
            if i in list_primes:
                assert self.pg.is_prime(i) == True, "%d was misclassified as NOT prime" % i
            else:
                assert self.pg.is_prime(i) == False, "%d was misclassified as prime" % i

    def test_message_transmission_controlledkeys(self):
        rigged = crypto.RSA(8, p=11, q=3, e=3)
        jane = agent.Agent(c=rigged)
        assert jane.get_public_key() == (33, 3), jane.get_public_key()
        assert jane.c.d == 7
        y = self.alice.encrypt_message(7, jane.get_public_key())
        p = jane.decrypt_message(y)
        assert p == 7

    def test_message_transmission_randomkeys(self):
        y = self.alice.encrypt_message(7, self.bob.get_public_key())
        p = self.bob.decrypt_message(y)
        print("Decrypted: %d" % p)
        assert p == 7


if __name__ == '__main__':
    unittest.main()
