from sage.all import *
from number_theory_functions import *
from utils import *
from factorization_algorithms.factorization_algorithm import factorization_algorithm


@factorization_algorithm
def dixon(N, B=None, H=None, MAX_IT=10**9, MIN_B=2, MAX_B=10**8, debug=False):
    if B is None:
        B = L_notation(N, alpha=1/2, c=sqrt(2)/2)
    B = clamp(MIN_B, B, MAX_B)

    big_prime_limit = B**2

    if debug:
        print(f"N: {N}")
        print(f"B: {B}")

    base = prime_sieve(B)
    L = len(base)

    if debug:
        print("L", L)

    if H is None:
        H = L

    relations, big_prime = set[Relation](), dict[Relation]()
    it = 0
    cnt = 0
    while len(relations) < L + 2 and it <= MAX_IT:
        it += 1

        if debug and it == MAX_IT:
            print("MAX_IT reached")

        z = randint(2, N-1)
        w = z**2 % N

        if debug and it % 1_000 == 0:
            print(f"w:{w} H:{H} |B|:{len(base)} |B|/H:{len(base) / H} cnt:{cnt} it:{it} cnt/it:{cnt/it}")

        factorization, remaining = factor_with_base(base, w)
        factorization = vector(GF(2), factorization, sparse=True)

        if remaining == 1:
            relations.add(Relation(A=z, Q=w, factorization=factorization))
        elif remaining < big_prime_limit and is_prime(remaining):
            if remaining in big_prime:
                relations.add(Relation(
                    A=(z * big_prime[remaining].A) % N,
                    Q=w * big_prime[remaining].Q,
                    factorization=factorization + big_prime[remaining].factorization,
                ))
                del big_prime[remaining]
            else:
                big_prime[remaining] = Relation(A=z, Q=w, factorization=factorization)

    if debug:
        total_data = sum([(len(str(rel.factorization)) + len(str(rel.A)) + len(str(rel.Q))) for rel in relations])
        print("data:", total_data/1000.0, "Kb")

    return factorize_N_with_elimination_on_factorization_matrix(N, L, relations)
