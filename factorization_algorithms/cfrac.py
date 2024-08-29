from sage.all import *
from number_theory_functions import *
from utils import *
from factorization_algorithms.factorization_algorithm import factorization_algorithm


@factorization_algorithm
def cfrac(N, K=1, B=None, MIN_B=2, MAX_B=10**9, MAX_IT=10**6, debug=False):
    if B is None:
        B = L_notation(K*N, alpha=1/2, c=1/2)
    B = clamp(MIN_B, B, MAX_B)

    big_prime_limit = B**2

    if debug:
        print(f"B: {B}")

    primes = prime_sieve(B)
    base = list(filter(
        lambda p: p == 2 or legendre_symbol(K*N, p) == +1,
        primes
    ))
    L = len(base)

    relations, big_prime = set[Relation](), dict[Relation]()

    g = isqrt(K*N)
    Q2, r2, A2 = K*N, g, 1       # index -1
    Q1, q1, r1, A1 = 1, g, 0, g  # index 0

    L += 1 # added -1 to base
    i = 1           
    it = 0
    while len(relations) < L + 2 and it <= MAX_IT:
        it += 1
        
        if debug and it == MAX_IT:
            print("MAX_IT reached")

        Q0 = Q2 + q1*(r1 - r2)
        G0 = 2*g - r1
        q0 = floor(G0/Q0)
        r0 = G0 - q0*Q0
        A0 = (q0*A1 + A2) % N

        if debug and it % 1000 == 0:
            print(len(relations)/L, len(str(Q0)))

        factorization, remaining = factor_with_base(base, abs(Q0))
        factorization = vector(
            GF(2),
            vector_concat(
                factorization,
                vector([1 if Q0 < 0 else 0])
            ),
            sparse=True
        )
        if remaining == 1:
            relations.add(Relation(A=A1, Q=Q0, factorization=factorization))
        elif remaining < big_prime_limit and is_prime(remaining):
            if remaining in big_prime:
                relations.add(Relation(
                    A=(A1 * big_prime[remaining].A) % N,
                    Q=Q0 * big_prime[remaining].Q,
                    factorization=factorization + big_prime[remaining].factorization,
                ))
                del big_prime[remaining]
            else:
                big_prime[remaining] = Relation(A=A1, Q=Q0, factorization=factorization)

        i += 1
        Q2, r2, A2 = Q1, r1, A1
        Q1, q1, r1, A1 = Q0, q0, r0, A0

    if debug:
        total_data = sum([(len(str(rel.factorization)) + len(str(rel.A)) + len(str(rel.Q))) for rel in relations])
        print("data:", total_data/1000.0, "Kb")

    return factorize_N_with_elimination_on_factorization_matrix(N, L, relations)
