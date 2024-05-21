import time
import multiprocessing
import math
from joblib import Parallel, delayed

# Expensive function
def expensive_function(x):
    return math.factorial(x)

RANGE = 20000

"""
Multiprocessing took 28.59 seconds
Without multiprocessing took 75.51 seconds
Joblib took 19.42 seconds
"""

if __name__ == "__main__":
    multiprocessing.freeze_support()
    # With multiprocessing

    start_time = time.time()
    with multiprocessing.Pool() as pool:
        results_with_multiprocessing = pool.map(expensive_function, range(RANGE))
    end_time = time.time()
    print(f"Multiprocessing took {end_time - start_time:.2f} seconds")

    # Without multiprocessing
    start_time = time.time()
    results_without_multiprocessing = [expensive_function(x) for x in range(RANGE)]
    end_time = time.time()
    print(f"Without multiprocessing took {end_time - start_time:.2f} seconds")

    # With joblib
    start_time = time.time()
    results_with_joblib = Parallel(n_jobs=-1)(delayed(expensive_function)(x) for x in range(RANGE))
    end_time = time.time()
    print(f"Joblib took {end_time - start_time:.2f} seconds")
