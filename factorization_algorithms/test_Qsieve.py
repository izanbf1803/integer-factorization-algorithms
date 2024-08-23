from sage.all import *
from number_theory_functions import *
from utils import *
from factorization_algorithms.Qsieve import Qsieve


# def Qsieve_case(N):
#     d = Qsieve(N=N)
#     if proper_divisor(N, d):
#         return True
#     return False

# def test_Qsieve_fixed():
#     assert Qsieve_case(10007 * 10009)

# def test_Qsieve_randomized_semiprime():
#     ROUNDS = 1
#     sizes = [5, 6, 7, 8] * ROUNDS + [10]
#     for size in sizes:
#         assert Qsieve_case(
#             random_prime(lbound=10**size//2, n=10**size) * random_prime(lbound=10**size//2, n=10**size)
#         )

# def test_cfrac_randomized_number():
#     ROUNDS = 1
#     sizes = [7, 8, 9] * ROUNDS + [10]
#     for size in sizes:
#         assert Qsieve_case(randint_non_prime(10**size//2, 10**size))
