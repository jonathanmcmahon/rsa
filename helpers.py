"""Helper functions for an RSA cryptosystem implementation."""
import math


def extended_euclid(a, b):
    """Extended Euclid's algorithm."""
    if b == 0:
        return 1, 0, a
    x, y, d = extended_euclid(b, a % b)
    return y, x - math.floor(a / b) * y, d


def mod_mult_inverse(a, n):
    x, y, d = extended_euclid(a, n)
    if d == 1:
        if x < 0:
            x = x + n
        # The definition of the modular multiplicative inverse of a wrt n:
        assert (a * x) % n == 1
        return x
    # If d != 1, then no mod multiplicative inverse exists
    return None


def relatively_prime(a, b):
    """Determine if two numbers a and b are relatively prime."""
    _, _, d = extended_euclid(a, b)
    # a and b are relatively prime if gcd(a, b) = 1
    if d == 1:
        return True
    return False
