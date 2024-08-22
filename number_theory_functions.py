from sage.all import *
from sage.misc.functional import N as NUM 


def ilog(b, N):
    ans = 0
    while N >= b:
        ans += 1
        N //= b
    return ans


def ceil_sqrt(N):
    s = isqrt(N)
    while s**2 < N:
        s += 1
    return s


def is_square(N):
    s = isqrt(N)
    return s**2 == N


def prime_sieve(N):
    primes = []
    isprime = [True] * N
    isprime[0] = isprime[1] = False
    for i in range(2, N):
        if isprime[i]:
            primes.append(i)
            for j in range(2*i, N, i):
                isprime[j] = False
    return primes


def factor_with_base(base, N, CFRAC_EAS=None):
    # returns a tuple (factorization, remaining part of N)
    L = len(base)
    v = vector(ZZ, L, sparse=True)
    for i in range(L):
        while N % base[i] == 0:
            N //= base[i]
            v[i] += 1
        if (CFRAC_EAS is not None) and (i in CFRAC_EAS) and (N > CFRAC_EAS[i]):
            return (v, N)
    return (v, N)


def number_from_factorization(factorization):
    n = 1
    for e in factorization:
        n *= e[0]**e[1]
    return n


def compute_with_base(base, v, M=None):
    L = len(base)
    assert len(base) == len(v)
    x = 1
    for i in range(L):
        if M is None:
            x *= base[i]**Integer(v[i])
        else:
            x = x * power_mod(base[i], Integer(v[i]), M) % M
    return x


def square_root_mod_p(a, p):
    # Uses the Tonelli-Shanks algorithm
    a, p = map(Integer, (a, p))
    
    if p == 2:
        return [a % 2]

    if kronecker(a, p) != 1:
        return None
    
    v = p-1
    e = 0
    while v % 2 == 0:
        v //= 2
        e += 1
        
    q = (p-1)/2**e
    
    z = None
    while z is None:
        k = randint(1, p-1)
        z = power_mod(k, q, p)
        if kronecker(z, p) != -1:
            z = None
    
    def S(a, b):
        # assert power_mod(a, (p-1)/2**b, p) == 1
        if b == e:
            return 0
        else:
            if power_mod(a, (p-1)/2**(b+1), p) == 1:
                return S(a, b+1)
            else:
                a_ = a * power_mod(z, 2**b, p) % p
                s_ = S(a_, b+1)
                return 2**(b-1) * q + s_
            
    s = S(a, 1)
    x = power_mod(a, (q+1)/2, p) * power_mod(z, s, p) % p
    x_ = -x % p
    
    # assert x**2 % p == a, x_**2 % p == a
    
    return [x, x_]
            
    


def L_notation(N, alpha=1, c=1):
    n = NUM(N, digits=10**4) # use 10000 digits for precise computation
    return ceil(
        exp( c * log(n)**alpha * log(log(n))**(1-alpha) )
    )
