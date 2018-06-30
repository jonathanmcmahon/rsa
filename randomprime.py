"""A random prime number generator."""
import random


def prime_test_naive(num):
    for i in range(2, (num / 2) + 1):
        if num % i == 0:
            return False
    return True


class RandomPrimeGenerator:

    def __init__(self):
        pass

    @staticmethod
    def generate(bits):
        max = 2 ** bits
        p = 4
        while not RandomPrimeGenerator.is_prime(p):
            p = random.randint(3, max)
        return p

    @staticmethod
    def is_prime(num, f=prime_test_naive):
        return f(num)


