"""Unit tests for RSA cryptosystem and related modules."""
import unittest
import helpers as util
import rsa
import randomprime as rp


class TestUtilFunctions(unittest.TestCase):

    VERBOSE = True

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
        r = rsa.RSA(8, verbose=self.VERBOSE)
        r.p = 2
        r.q = 4
        with self.assertRaises(Exception):
            r._generate_public_key()


if __name__ == '__main__':
    unittest.main()
