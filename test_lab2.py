import pytest
from lab2 import prime_num_generator

def test_first_twelve_primes():
    generator = prime_num_generator()
    first_twelve_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for i in range(12):
        assert next(generator) == first_twelve_numbers[i]

    generator1 = prime_num_generator()
    for i in range(100):
        next(generator1)
    assert next(generator1) == 547