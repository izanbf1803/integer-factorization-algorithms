from sage.all import *
from number_theory_functions import *
from utils import *
from factorization_algorithms.pollard_rho import pollard_rho


def pollard_rho_case(N):
    d = pollard_rho(N=N)
    return proper_divisor(N, d)

def test_pollard_rho_fixed():
    assert pollard_rho_case((10**9+7) * (10**9+9))

def test_pollard_rho_randomized_semiprime():
    ROUNDS = 3
    sizes = [5, 10, 12] * ROUNDS
    for size in sizes:
        assert pollard_rho_case(
            random_prime(lbound=10**size//2, n=10**size) * random_prime(lbound=10**size//2, n=10**size)
        )

def test_pollard_rho_randomized_number():
    ROUNDS = 3
    sizes = [10, 15, 20] * ROUNDS
    for size in sizes:
        assert pollard_rho_case(randint_non_prime(10**size//2, 10**size))
