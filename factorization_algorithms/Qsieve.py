from collections import defaultdict
from sage.all import *
from number_theory_functions import *
from utils import *
from factorization_algorithms.factorization_algorithm import factorization_algorithm
from sieve import polynomial_sieve_range


@factorization_algorithm
def Qsieve(N, B=None, MIN_B=2, MAX_B=10**9, step = 10**6, debug=False):
    f = lambda x: x**2 - N
    f_ = lambda x: 2*x
    s = ceil_sqrt(N)

    if B is None:
        B = L_notation(N, alpha=1/2, c=1/2)
    B = clamp(MIN_B, B, MAX_B)

    if debug:
        print(f"B: {B}")

    base = list(filter(
        lambda p: p == 2 or legendre_symbol(N, p) == 1,
        prime_sieve(B)
    ))

    L = len(base)
    I = s
    J = s+step-1

    relations = set[Relation]()
    
    while len(relations) < L + 2:
        if debug:
            print("starting polynomial_sieve_range", I, J)
        factorized = polynomial_sieve_range(f, base, I, J, specialized=True, debug=False)
        if debug:
            print("ended polynomial_sieve_range")
        
        for i in range(I, J+1):            
            if factorized[i].remaining == 1:
                relations.add(Relation(
                    A=factorized[i].x,
                    Q=factorized[i].image,
                    factorization=vector(
                        GF(2),
                        factorized[i].factorization,
                        sparse=True
                    )
                ))
                if len(relations) >= L + 2:
                    break
                    
        if debug:
            print("R,L:", len(relations), L)
        
        I += step
        J += step
    
    if debug:
        total_data = sum([(len(str(rel.factorization)) + len(str(rel.A)) + len(str(rel.Q))) for rel in relations])
        print("data:", total_data/1000.0, "Kb")

    return factorize_N_with_elimination_on_factorization_matrix(N, L, relations)
