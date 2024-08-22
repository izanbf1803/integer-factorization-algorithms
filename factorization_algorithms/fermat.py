from sage.all import *
from number_theory_functions import *
from utils import *
from factorization_algorithms.factorization_algorithm import factorization_algorithm


@factorization_algorithm
def fermat(N):
    x = ceil_sqrt(N)
    while not is_square(x**2 - N):
        x += 1
    return x - isqrt(x**2 - N)
