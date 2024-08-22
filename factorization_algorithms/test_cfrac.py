from sage.all import *
from number_theory_functions import *
from utils import *
from factorization_algorithms.cfrac import cfrac


def cfrac_case(N):
    Ks = [1, 3, 5, 7, 257]
    for K in Ks:
        d = cfrac(N=N, K=K, MAX_IT=100_000)
        if proper_divisor(N, d):
            return True
    return False

def test_cfrac_fixed():
    assert cfrac_case((10**9+7) * (10**9+9))

def test_cfrac_randomized_semiprime():
    ROUNDS = 3
    sizes = [5, 6, 7, 8] * ROUNDS + [11, 12]
    for size in sizes:
        assert cfrac_case(
            random_prime(lbound=10**size//2, n=10**size) * random_prime(lbound=10**size//2, n=10**size)
        )

def test_cfrac_randomized_number():
    ROUNDS = 3
    sizes = [10, 15, 20] * ROUNDS + [25]
    for size in sizes:
        assert cfrac_case(randint_non_prime(10**size//2, 10**size))
