from sage.all import *
from number_theory_functions import *
from utils import *
from factorization_algorithms.pollard_p_1 import pollard_p_1


def pollard_p_1_case(N):
    d = pollard_p_1(N=N)
    return proper_divisor(N, d)

def test_pollard_p_1_fixed():
    assert pollard_p_1_case(113 * 339339663889 * 26333829143185762927)

def test_pollard_p_1_randomized_semiprime():
    ROUNDS = 3
    sizes = [5, 6, 7] * ROUNDS
    for size in sizes:
        assert pollard_p_1_case(
            random_prime(lbound=10**size//2, n=10**size) * random_prime(lbound=10**size//2, n=10**size)
        )

def test_pollard_p_1_randomized_number():
    ROUNDS = 3
    sizes = [5, 10, 12] * ROUNDS
    for size in sizes:
        assert pollard_p_1_case(randint_non_prime(10**size//2, 10**size))
