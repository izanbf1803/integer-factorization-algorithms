from sage.all import *
from number_theory_functions import *
from utils import *
from factorization_algorithms.pollard_p_1 import pollard_p_1


def pollard_p_1_case(N):
    d = pollard_p_1(N=N)
    return proper_divisor(N, d)

def test_pollard_p_1_fixed():
    assert pollard_p_1_case(113 * 339339663889 * 26333829143185762927)

def test_pollard_p_1_smooth():
    ROUNDS = 3
    B = 10**4
    factors = [5, 10, 100] * ROUNDS
    for n in factors:
        prod = Integer(1)
        for _ in range(n):
            prod *= random_prime(B)
        assert pollard_p_1_case(prod)
