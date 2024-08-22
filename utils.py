from sage.all import *
from dataclasses import dataclass


@dataclass
class Relation: 
    # Represents a relation of the type A^2 = Q (mod N), with Q factorized
    A: int
    Q: int
    factorization: vector

    def __hash__(self):
        return hash(str(self))
    

def clamp(l, x, r):
    if x < l:
        return l
    elif x > r:
        return r
    else:
        return x


def dicts_keys_delete(dicts, keys):
        for dic in dicts:
            for key in keys:
                if key in dic:
                    del dic[key]


def vector_concat(v, w):
    return vector(v.list() + w.list())


def proper_divisor(N, d):
    return 1 < d < N and N % d == 0


def randint_non_prime(l, r):
    it = 0
    N = randint(l, r)
    while is_prime(N):
        if it > 100_000:
            raise Exception("bad randint_non_prime interval")
        N = randint(l, r)
        it += 1
    return N


def omega_p(N, p):
    cnt = 0
    while N % p == 0:
        N //= p
        cnt += 1
    return cnt


def factorize_N_with_elimination_on_factorization_matrix(N, L, relations):
    # L is the base length for the factorizations
    relations = list(relations)

    R = len(relations)
    M = matrix(GF(2), R, L+R, sparse=True)
    j = 0
    for i in range(R):
        M[j,L+j] = 1
        for p in range(L):
            if relations[i].factorization[p] % 2 == 1:
                M[j,p] = 1
        j += 1

    M = M.echelon_form()

    for i in range(R):
        if all(M[i,j] == 0 for j in range(L)):
            prodQ = 1
            prodA = 1
            for j in range(L, L+R):
                if M[i,j] % 2 == 1:
                    prodQ *= relations[j-L].Q
                    prodA *= relations[j-L].A
                    prodA %= N
            x = prodA
            y = isqrt(prodQ)
            assert (y*y == prodQ)
            d = gcd(x-y, N)
            if proper_divisor(N, d):
                return d
    
    return 1 # factorization failed
