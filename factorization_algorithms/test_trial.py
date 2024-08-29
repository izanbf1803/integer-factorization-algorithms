from sage.all import *
from number_theory_functions import *
from utils import *
from factorization_algorithms.trial import trial


def trial_case(N):
    d = trial(N=N)
    return proper_divisor(N, d)

def test_prime_power_detection():
    assert trial_case((10**9 + 7)**1000)

def test_trial_fixed():
    assert trial_case(113 * 339339663889 * 26333829143185762927)

def test_trial_randomized_semiprime():
    ROUNDS = 3
    sizes = [5, 6, 7] * ROUNDS
    for size in sizes:
        assert trial_case(
            random_prime(lbound=10**size//2, n=10**size) * random_prime(lbound=10**size//2, n=10**size)
        )

def test_trial_randomized_number():
    ROUNDS = 3
    sizes = [5, 10, 12] * ROUNDS
    for size in sizes:
        assert trial_case(randint_non_prime(10**size//2, 10**size))
