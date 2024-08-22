from sage.all import *
from number_theory_functions import *
from utils import *
from factorization_algorithms.factorization_algorithm import factorization_algorithm


@factorization_algorithm
def trial(N):
    for i in range(2, isqrt(N)+1):
        if N % i == 0:
            return i
    return 1
