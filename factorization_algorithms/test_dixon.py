from sage.all import *
from number_theory_functions import *
from utils import *
from factorization_algorithms.dixon import dixon


def dixon_case(N):
    d = dixon(N=N, MAX_IT=1_000_000)
    return proper_divisor(N, d)

def test_dixon_fixed():
    assert dixon_case(135461 * 932131)

def test_dixon_randomized_semiprime():
    ROUNDS = 3
    sizes = [3, 4] * ROUNDS
    for size in sizes:
        assert dixon_case(
            random_prime(lbound=10**size//2, n=10**size) * random_prime(lbound=10**size//2, n=10**size)
        )

def test_dixon_randomized_number():
    ROUNDS = 3
    sizes = [5, 8] * ROUNDS
    for size in sizes:
        assert dixon_case(randint_non_prime(10**size//2, 10**size))
