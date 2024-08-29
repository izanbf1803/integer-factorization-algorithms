from sage.all import *
from number_theory_functions import *
from utils import *
from factorization_algorithms.cfrac import cfrac


def cfrac_case(N):
    Ks = [(1, 100_000), (3, 100_000), (5, 100_000), (7, 100_000), (257, 10_000_000), (197293, 10_000_000)]  
    for K, MAX_IT in Ks:
        d = cfrac(N=N, K=K, MAX_IT=MAX_IT)
        if proper_divisor(N, d):
            return True
    return False

def test_cfrac_fixed():
    assert cfrac_case((10**9+7) * (10**9+9))

def test_cfrac_randomized_semiprime():
    ROUNDS = 3
    sizes = [5, 6, 7] * ROUNDS + [8]
    for size in sizes:
        assert cfrac_case(
            random_prime(lbound=10**size//2, n=10**size) * random_prime(lbound=10**size//2, n=10**size)
        )

def test_cfrac_randomized_number():
    ROUNDS = 3
    sizes = [10, 15, 20] * ROUNDS + [25]
    for size in sizes:
        assert cfrac_case(randint_non_prime(10**size//2, 10**size))
