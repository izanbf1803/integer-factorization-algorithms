from collections import defaultdict
from sage.all import *
from number_theory_functions import *
from utils import *
from sage.rings.finite_rings.integer_mod import square_root_mod_prime


class SieveFactorization: 
    x: int
    image: int
    remaining: int
    factorization: defaultdict[int] # stores the power of each factor

    def __init__(self, x, image, base):
        self.x = x
        self.image = image
        self.remaining = image
        self.factorization = vector(ZZ, len(base), sparse=True)

    def __str__(self):
        return f"SieveFactorization(x={self.x},image={self.image}," + \
               f"remaining={self.remaining},factorization={self.factorization})"

    def __hash__(self):
        return hash(str(self))


def hensel_lifting(f, f_, p_e, r):
#     assert k > 0 and f(r) % p_k == 0 and f_(r) % p != 0
    a = inverse_mod(Integer(f_(r)), p_e)
#     assert a * f_(r) % p_k_1 == 1
    s = (r - Integer(f(r)) * a) % p_e
#     assert f(s) % p_k_1 == 0
    return Integer(s)

def square_roots_mod_p(N, p):
    if legendre_symbol(N, p) == 1:
        r = ZZ( square_root_mod_prime(Mod(N, p)) )
        r2 = (-r) % p
        assert r**2 % p == N % p and r2**2 % p == N % p
        return [Integer(r), Integer(r2)]
    return []


def eratosthenes(N):
    prime = [True for _ in range(N+1)]
    prime[0] = prime[1] = False
    P = []
    for i in range(2, N+1):
        if prime[i]:
            P.append(i)
            for j in range(i*i, N+1, i):
                prime[j] = False
    return P


def eratosthenes_range(I, J):
    S = ceil_sqrt(J)
    P = eratosthenes(S)
    prime = {i: True for i in range(I, J+1)}
    for p in P:
        i0 = p * ceil(I/p)
        for i in range(i0, J+1, p):
            prime[i] = False
    P_I_J = []
    for i in range(I, J+1):
        if prime[i]:
            P_I_J.append(i)
    return P_I_J


def factor_eratosthenes(N):
    prime = [True for _ in range(N+1)]
    prime[0] = prime[1] = False
    L = {i: [] for i in range(2, N+1)}
    for i in range(2, N+1):
        if prime[i]:
            L[i].append((i, 1))
            for j in range(2*i, N+1, i):
                prime[j] = False
                L[j].append( (i, omega_p(j, i)) )
    for i in range(2, N+1):
        k = i
        for f in L[i]:
            for _ in range(f[1]):
                k //= f[0]
        if k > 1:
            L[i].append( (k, 1) )
    return L


def factor_eratosthenes_range(I, J):
    S = ceil_sqrt(J)
    P = eratosthenes(S)
    L = {i: [] for i in range(I, J+1)}
    for p in P:
        i0 = p * ceil(I/p)
        for i in range(i0, J+1, p):
            L[i].append( (p, omega_p(i, p)) )
    for i in range(I, J+1):
        k = i
        for f in L[i]:
            for _ in range(f[1]):
                k //= f[0]
        if k > 1:
            L[i].append( (k, 1) )
    return L


def polynomial_sieve_range(f, base, I, J, specialized=False, debug=False):
    # returns a list of SieveFactorization of f(x) for all x in [I, J]
    sieve = {i: SieveFactorization(i, f(i), base) for i in range(I, J+1)}
    for idx in range(len(base)):
        p = base[idx]
        if specialized:
            # specialized for x^2 - N
            N = -f(0)
            sqrtN = square_root_mod_p(N, p)
            if sqrtN is None:
                R = []
            else:
                R = sqrtN
            if debug:
                print(N, p, R)
        else:
            # in general for all polynomials, slower
            F = ZZ['x']
            x = polygen(F, 'x')
            f_p = f(x)
            if debug:
                print(p, f, f_p, IntegerModRing(p)['x'](f_p))
            if IntegerModRing(p)['x'](f_p) != 0:
                R = [Integer(e[0]) for e in IntegerModRing(p)['x'](f_p).roots()]
            else:
                R = list(range(p))
        for root in R:
            i0 = I + (root - I) % p
            if debug:
                print(I, J, i0, (root - I) % p, type(i0))
            for i in range(i0, J+1, p):
                if debug:
                    print(I, J, i)
                while sieve[i].remaining % p == 0:
                    sieve[i].factorization[idx] += 1
                    sieve[i].remaining //= p
    return sieve
