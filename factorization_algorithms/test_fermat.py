from sage.all import *
from number_theory_functions import *
from utils import *
from factorization_algorithms.fermat import fermat


def fermat_case(N):
    d = fermat(N=N)
    return proper_divisor(N, d)

def test_fermat_fixed():
    assert fermat_case((10**9+7) * (10**9+9))
    assert fermat_case(1000000000000000000000000001443 * 1000000000000000000000000001629)

def test_fermat_randomized_semiprime():
    ROUNDS = 3
    sizes = [5, 6, 7] * ROUNDS
    for size in sizes:
        assert fermat_case(
            random_prime(lbound=10**size//2, n=10**size) * random_prime(lbound=10**size//2, n=10**size)
        )

def test_fermat_randomized_number():
    ROUNDS = 3
    sizes = [5, 6, 7] * ROUNDS
    for size in sizes:
        assert fermat_case(randint_non_prime(10**size//2, 10**size))
