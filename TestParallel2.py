import numpy as np
from joblib import Parallel, delayed
import multiprocessing
from math import ceil

N = 10 # Some number
inputs = range(1,N,2)
num_cores = multiprocessing.cpu_count()

def processInput(n): # toy function
    return n

resultsN = []
# your original solution with an additional loop that needs
# to be parallelized
for m in range(1,N,2):  
    add = Parallel(n_jobs=num_cores)(delayed(processInput)(n) for n in inputs)
    resultsN = add + resultsN
resultsN = sum(resultsN)
print(resultsN)

# solution with only one layer of parallelization
ext_inputs = np.repeat(inputs,ceil(m/2.0)).tolist()
add = Parallel(n_jobs=num_cores)(delayed(processInput)(n) for n in ext_inputs)
resultsN = sum(add)
print(resultsN)