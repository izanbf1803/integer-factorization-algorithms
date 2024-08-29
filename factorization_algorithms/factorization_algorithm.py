from sage.all import *
from number_theory_functions import is_power

def factorization_algorithm(func):
    def wrapper_factorization_algorithm(*args, **kwargs):
        if 'N' in kwargs.keys():
            N = kwargs['N']
        else:
            N = args[0]

        if is_prime(N):
            return 1
        elif N % 2 == 0:
            return 2
        else:
            N_is_power, _, root = is_power(N)
            if N_is_power:
                return root
            else:
                return func(*args, **kwargs) # execute factorization algorithm
        
    return wrapper_factorization_algorithm
