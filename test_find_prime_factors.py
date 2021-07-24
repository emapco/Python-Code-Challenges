from unittest import TestCase


def get_product(factors):
    product = 1
    for factor in factors:
        product *= factor
    return product


# Test will pass if the product of the factors returned
# is equal to the number that was factorized
class Test(TestCase):
    def test_prime_factorize(self):
        from find_prime_factors import prime_factorize
        self.assertEqual(get_product(prime_factorize(100)), 100)
        self.assertEqual(get_product(prime_factorize(13)), 13)
        self.assertEqual(get_product(prime_factorize(1043657)), 1043657)
