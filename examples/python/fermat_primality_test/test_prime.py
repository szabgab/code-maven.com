import prime
import random


def test_coprime():
    random.seed(1)
    assert prime.get_coprime(10) == 9
    assert prime.get_coprime(10) == 1

    assert prime.get_coprime(100000) == 64937

def test_fermat_primality():
    random.seed(1)
    assert prime.fermat_primality(1000) == False


