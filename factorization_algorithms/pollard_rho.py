from sage.all import *
from number_theory_functions import *
from utils import *
from factorization_algorithms.factorization_algorithm import factorization_algorithm


@factorization_algorithm
def pollard_rho(N):
    g = lambda x: (x**2 + 1) % N
    x0 = randint(0, N-1)
    a = g(x0)
    b = g(g(x0))
    while gcd(abs(a-b), N) == 1:
        a = g(a)
        b = g(g(b))
    return gcd(abs(a-b), N)
