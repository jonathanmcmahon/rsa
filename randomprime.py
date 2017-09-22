"""A random prime number generator."""


def prime_test_naive(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


class RandomPrimeGenerator:

    def __init__(self):
        pass

    @staticmethod
    def generate(bits):
        # max = (2 ** bits) - 1
        # while prime.isprime()
        # return prime
        return 0b00001101

    @staticmethod
    def is_prime(num, f=prime_test_naive):
        return f(num)


