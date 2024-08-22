from sage.all import *
from number_theory_functions import *
from utils import *
from factorization_algorithms.factorization_algorithm import factorization_algorithm


@factorization_algorithm
def pollard_p_1(N, B=10**5, RONDES=1000):
    primes = prime_sieve(B)
    for ronda in range(RONDES):
        a0 = 0
        while gcd(a0, N) != 1:
            a0 = randint(2, N-1)
        l = 2
        r = B
        while l <= r:
            a = a0
            b = (l+r)//2
            for q in primes:
                if q > B:
                    break
                a = power_mod(a, q**ilog(q, b), N)
                d = gcd(abs(a-1), N)
                if 1 < d < N:
                    return d
            if d == 1:
                l = b + 1
            else:
                r = b - 1
    return 1
