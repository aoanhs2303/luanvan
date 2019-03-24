from joblib import Parallel, delayed
import multiprocessing
import datetime


start = datetime.datetime.now()
inputs = range(10)


def processInput(i):
    return i * i


num_cores = multiprocessing.cpu_count()
print(num_cores)

results = Parallel(n_jobs=num_cores)(delayed(processInput)(i) for i in inputs)
print(results)
end = datetime.datetime.now()
print(end - start)


