import unittest
import helpers as util
import rsa
import randomprime as rp


class TestUtilFunctions(unittest.TestCase):

    def test_relatively_prime(self):
        self.assertEqual(util.relatively_prime(12, 13), True)
        self.assertEqual(util.relatively_prime(12, 14), False)
        self.assertEqual(util.relatively_prime(20, 79), True)
        self.assertEqual(util.relatively_prime(3, 62), True)
        self.assertEqual(util.relatively_prime(5, 23), True)
        self.assertEqual(util.relatively_prime(21, 91), False)

if __name__ == '__main__':
    unittest.main()
