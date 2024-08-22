from sage.all import *

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
            return func(*args, **kwargs)
        
    return wrapper_factorization_algorithm
