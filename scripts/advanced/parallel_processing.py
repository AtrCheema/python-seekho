"""
=========================
7.2. Parallel Processing
=========================

This lesson demonstrates various ways of parallelizing the python code on cpu cores.
"""

import time
from itertools import product
import concurrent.futures as cf
from multiprocessing import cpu_count, Pool

import numpy as np
import pandas as pd
import scipy.stats as ss
from numpy.random import default_rng
from joblib import Parallel, delayed

# %%

print(cpu_count())

# %%
# Decide the number of cpu processes to use to paralllize the code.
# Parallelizing the code makes sense if we have at least 2 cores.

cpus = max(2, cpu_count()//2)
print(cpus)

# %%
# We have two versions of `cramers_v` function. The first version takes a single
# argument `indices` as input. This function then uses the ``data`` from global scope
# to get two arrays (x and y) and calculates Cramers' v value.The second function,
# on the other hand uses the two arrays (x and y) as innput and calcuates Cramers` v
# for them.

def cramers_v(indices):
    i, j = indices
    x, y = data.loc[:, i], data.loc[:, j]
    return _cramers_v(x, y)


def cramers_v_data(x, y):
    return _cramers_v(x, y)


def _cramers_v(x, y):
    confusion_matrix = pd.crosstab(x, y)
    chi2 = ss.chi2_contingency(confusion_matrix)[0]
    n = confusion_matrix.sum().sum()
    phi2 = chi2 / n
    r, k = confusion_matrix.shape
    phi2corr = max(0, phi2 - ((k - 1) * (r - 1)) / (n - 1))
    rcorr = r - ((r - 1) ** 2) / (n - 1)
    kcorr = k - ((k - 1) ** 2) / (n - 1)
    return np.sqrt(phi2corr / min((kcorr - 1), (rcorr - 1)))

# %%
# Create data with categorical/string values. Increasing the number
# of columns will increase the number of for loops.

columns = 20  # total number fo for loops will be columns * columns
data = pd.DataFrame(np.random.randint(1, 20, (5000, columns)).astype(str))

print(data.shape)

# %%
# Sequential Implementation
# =========================================

def without_pp():
    start = time.time()
    results = np.full((data.shape[1], data.shape[1]), fill_value=np.nan)
    for i in range(data.shape[1]):
        for j in  range(data.shape[1]):
            results[i,j] = cramers_v((i,j))
    print(round(time.time() - start, 2), 'seconds in sequential mode')
    return results


# %%
# Parallel Implementations
# =============================
# We will 4 different ways ways of parallelizing the code.

# %%
# ProcessPoolExecutor from concurrent
# -------------------------------------

def with_ppe():

    start = time.time()
    with cf.ProcessPoolExecutor(max_workers=cpus) as executor:
        list_of_cols = list(product(range(data.shape[1]), range(data.shape[1])))
        results = executor.map(
            cramers_v,
            list_of_cols
        )
    print(round(time.time() - start, 2), 'seconds with ProcessPoolExecutor')

    return results

# %%

def with_ppe_data():
    rng = default_rng(313)
    data_ = pd.DataFrame(rng.integers(1, 20, (5000, columns)).astype(str))

    start = time.time()
    with cf.ProcessPoolExecutor(max_workers=cpus) as executor:
        list_of_cols = list(product(range(data_.shape[1]), range(data_.shape[1])))
        list_of_x = [data_.loc[:, i] for (i, _) in list_of_cols]
        list_of_y = [data_.loc[:, j] for (_, j) in list_of_cols]
        results = executor.map(
            cramers_v_data,
            list_of_x,
            list_of_y
        )
    print(round(time.time() - start, 2), 'seconds with ProcessPoolExecutor (data)')
    return results

# %%
# ThreadPoolExecutor from concurrent
# ------------------------------------

def with_tpe():
    start = time.time()
    with cf.ThreadPoolExecutor(max_workers=cpus) as executor:
        list_of_cols = list(product(range(data.shape[1]), range(data.shape[1])))
        results = executor.map(
            cramers_v,
            list_of_cols
        )
    print(round(time.time() - start, 2), 'seconds with ThreadPoolExecutor')
    return results

# %%

def with_tpe_data():

    rng = default_rng(313)
    data_ = pd.DataFrame(rng.integers(1, 20, (5000, columns)).astype(str))

    start = time.time()
    with cf.ThreadPoolExecutor(max_workers=cpus) as executor:
        list_of_cols = list(product(range(data.shape[1]), range(data.shape[1])))
        list_of_x = [data_.loc[:, i] for (i,j) in list_of_cols]
        list_of_y = [data_.loc[:, j] for (i, j) in list_of_cols]

        results = executor.map(
            cramers_v_data,
            list_of_x,
            list_of_y
        )
    print(round(time.time() - start, 2), 'seconds with ThreadPoolExecutor (data)')
    return results

# %%
# Pool from multiprocessing
# -------------------------------------

def with_pool():

    start = time.time()
    with Pool(processes=cpus) as executor:
        list_of_cols = list(product(range(data.shape[1]), range(data.shape[1])))
        results = executor.map(
            cramers_v,
            list_of_cols,
        )
    print(round(time.time() - start, 2), 'seconds with Pool')

    return results

# %%
# The following function uses Pool but with two changes. First, the function
# cramers_v_data receives the actual arrays (of data) instead of indices. In this
# the function which we want to parallelize, does not uses any global variable/data.
# The second difference is that our function now receives two inputs instead of a
# single input.

def with_pool_data():

    rng = default_rng(313)
    data_ = pd.DataFrame(rng.integers(1, 20, (5000, columns)).astype(str))

    start = time.time()
    with Pool(processes=cpus) as executor:
        list_of_cols = list(product(range(data_.shape[1]), range(data_.shape[1])))
        list_of_xy = [(data_.loc[:, i], data_.loc[:, j]) for (i,j) in list_of_cols]
        results = executor.starmap(
            cramers_v_data,
            list_of_xy,
        )
    print(round(time.time() - start, 2), 'seconds with Pool (data)')
    return results

# %%
# Using joblib
# -------------

def with_joblib(backend="loky", verbose=0, batch_size="auto"):
    start = time.time()
    list_of_cols = list(product(range(data.shape[1]), range(data.shape[1])))
    results = Parallel(
        n_jobs=cpus, backend=backend, verbose=verbose, batch_size=batch_size)(
        delayed(cramers_v)(val) for val in list_of_cols)

    print(round(time.time() - start, 2), f'seconds with joblib backend {backend}')
    return results

# %%

def with_joblib_and_data(backend="loky", verbose=0, batch_size="auto"):

    rng = default_rng(313)
    data_ = pd.DataFrame(rng.integers(1, 20, (5000, columns)).astype(str))

    start = time.time()
    list_of_cols = list(product(range(data_.shape[1]), range(data_.shape[1])))
    results = Parallel(
        n_jobs=cpus, backend=backend, verbose=verbose, batch_size=batch_size)(
        delayed(cramers_v_data)(
            data_.loc[:, i], data_.loc[j]) for (i,j) in list_of_cols)

    print(round(time.time() - start, 2), f"seconds with joblib (data) backend {backend}")
    return results

# %%

if __name__ == "__main__":

    results_nopp = without_pp()

    results_ppe = with_ppe()
    results_ppe = np.array(list(results_ppe)).reshape(results_nopp.shape)
    print(np.allclose(results_nopp, results_ppe))

    res_ppe_data = with_ppe_data()
    res_ppe_data = np.array(list(res_ppe_data)).reshape(results_nopp.shape)

    results_tpe = with_tpe()
    results_tpe = np.array(list(results_tpe)).reshape(results_nopp.shape)
    print(np.allclose(results_nopp, results_tpe))

    res_tpe_data = with_tpe_data()
    res_tpe_data = np.array(list(res_tpe_data)).reshape(results_nopp.shape)
    print(np.allclose(res_ppe_data, res_tpe_data))

    results_pool = with_pool()
    results_pool = np.array(list(results_pool)).reshape(results_nopp.shape)
    print(np.allclose(results_nopp, results_pool))

    res_pool_data = with_pool_data()
    res_pool_data = np.array(list(res_pool_data)).reshape(results_nopp.shape)
    print(np.allclose(res_ppe_data, res_pool_data))

    results_joblib = with_joblib()
    results_joblib = np.array(results_joblib).reshape(results_nopp.shape)
    print(np.allclose(results_nopp, results_joblib))

    results_joblib = with_joblib(backend="multiprocessing")
    results_joblib = np.array(results_joblib).reshape(results_nopp.shape)
    print(np.allclose(results_nopp, results_joblib))

    results_joblib = with_joblib(backend="threading")
    results_joblib = np.array(results_joblib).reshape(results_nopp.shape)
    print(np.allclose(results_nopp, results_joblib))

    res_joblib_data = with_joblib_and_data(backend="loky")
    res_joblib_data = np.array(res_joblib_data).reshape(results_nopp.shape)
    print(np.allclose(res_ppe_data, res_joblib_data))

    res_joblib_data = with_joblib_and_data(backend="threading")
    res_joblib_data = np.array(res_joblib_data).reshape(results_nopp.shape)
    print(np.allclose(res_ppe_data, res_joblib_data))

# %%