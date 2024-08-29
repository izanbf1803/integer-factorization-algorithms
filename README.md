Requirements
============

Install Sage from conda-forge: https://doc.sagemath.org/html/en/installation/conda.html


Testing 
=======

To run the tests, activate the Sage environment in conda and run `python -m pytest -v` in the main folder.


Usage
=====

In general, once the requirements are satisfied, you can execute the algorithms in the following fashion:

```Python
from factorization_algorithms.algorithm import algorithm

algorithm(N, other_parameters)
```

As an example, let's factor `36416277516431290307` using both  pollard rho and continued fractions algorithm:

```Python
from factorization_algorithms.pollard_rho import pollard_rho
from factorization_algorithms.cfrac import cfrac

N = 36416277516431290307
print(pollard_rho(N), cfrac(N, K=257))
```
```
> 6681528299 5450291593
```

Seems to work, since `36416277516431290307 == 6681528299*5450291593`.
