"""
==========================
7.9 Speeding up with numba
==========================
"""

import os 
import time
from typing import Tuple
from multiprocessing import cpu_count
 
import sys
import numpy as np
from numba import numba
from numba import jit, float32, int32, prange
from numba.types import Tuple as nbTuple
from numba import get_num_threads, set_num_threads

# %%

print("Python version: ", sys.version)
print("numpy version: ", np.__version__)
print("numba version: ", numba.__version__)

# %% 
cpus = max(2, cpu_count()//2)
# os.environ['NUMBA_NUM_THREADS'] = str(cpus)  # Change it to the number of CPU cores you want to use
# set_num_threads(cpus)
print("Number of threads:", get_num_threads())

# %%

def prepare_data(
        data: np.ndarray,
        lookback: int,
        num_inputs: int = None,
        num_outputs: int = None,
        input_steps: int = 1,
        forecast_step: int = 0,
        forecast_len: int = 1,
) -> Tuple[np.ndarray, np.ndarray]:
    """

    """
    assert isinstance(data, np.ndarray)

    if num_inputs is None and num_outputs is None:
        raise ValueError("""
Either of num_inputs or num_outputs must be provided.
""")

    features = data.shape[1]
    if num_outputs is None:
        num_outputs = features - num_inputs

    if num_inputs is None:
        num_inputs = features - num_outputs

    assert num_inputs + num_outputs == features, f"""
num_inputs {num_inputs} + num_outputs {num_outputs} != total features {features}"""

    if len(data) <= 1:
        raise ValueError(f"Can not create batches from data with shape {data.shape}")

    time_steps = lookback

    examples = len(data)

    x = []
    y = []

    for i in range(examples - lookback * input_steps + 1 - forecast_step - forecast_len + 1):
        stx, enx = i, i + lookback * input_steps
        x_example = data[stx:enx:input_steps, 0:features - num_outputs]

        sty = (i + time_steps * input_steps) + forecast_step - input_steps
        eny = sty + forecast_len
        target = data[sty:eny, features - num_outputs:]

        x.append(np.array(x_example))
        y.append(np.array(target))

    if len(x)<1:
        raise ValueError(f"""
        no examples generated from data of shape {data.shape} with lookback 
        {lookback} input_steps {input_steps} forecast_step {forecast_step} forecast_len {forecast_len}
""")
    x = np.stack(x)
    # transpose because we want labels to be of shape (examples, outs, forecast_len)
    y = np.array([np.array(i, dtype=np.float32).T for i in y], dtype=np.float32)


    return x, y

# %%

@jit(nopython=True)
def prepare_data1(
        data: np.ndarray,
        lookback: int,
        num_inputs: int = None,
        num_outputs: int = None,
        input_steps: int = 1,
        forecast_step: int = 0,
        forecast_len: int = 1,
) -> tuple[np.ndarray, np.ndarray]:
    """
    Prepare input and output data for time series forecasting.
    """
    if num_inputs is None and num_outputs is None:
        raise ValueError("Either of num_inputs or num_outputs must be provided.")

    features = data.shape[1]
    if num_outputs is None:
        num_outputs = features - num_inputs

    if num_inputs is None:
        num_inputs = features - num_outputs

    if num_inputs + num_outputs != features:
        raise ValueError(f"num_inputs {num_inputs} + num_outputs {num_outputs} != total features {features}")

    if len(data) <= 1:
        raise ValueError(f"Cannot create batches from data with shape {data.shape}")

    examples = len(data)
    max_examples = examples - lookback * input_steps + 1 - forecast_step - forecast_len + 1
    if max_examples <= 0:
        raise ValueError(f"No examples generated from data of shape {data.shape} with lookback {lookback}, input_steps {input_steps}, forecast_step {forecast_step}, forecast_len {forecast_len}")

    x = np.empty((max_examples, lookback, num_inputs), dtype=data.dtype)
    y = np.empty((max_examples, forecast_len, num_outputs), dtype=data.dtype)

    for i in range(max_examples):
        x_start_idx = i
        x_end_idx = x_start_idx + lookback * input_steps
        y_start_idx = x_end_idx + forecast_step - input_steps
        y_end_idx = y_start_idx + forecast_len

        x[i] = data[x_start_idx:x_end_idx:input_steps, :num_inputs]
        y[i] = data[y_start_idx:y_end_idx, -num_outputs:]

    y = np.transpose(y, (0, 2, 1)).astype(np.float32)

    return x, y

# %%

@jit(nbTuple((float32[:, :, :], float32[:, :, :]))(float32[:, :], int32, int32, int32, int32, int32, int32), nopython=True)
def prepare_data2(
        data: np.ndarray,
        lookback: int,
        num_inputs: int,
        num_outputs: int,
        input_steps: int,
        forecast_step: int,
        forecast_len: int,
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Prepare input and output data for time series forecasting.
    """
    features = data.shape[1]

    if num_inputs + num_outputs != features:
        raise ValueError(f"num_inputs {num_inputs} + num_outputs {num_outputs} != total features {features}")

    if len(data) <= 1:
        raise ValueError(f"Cannot create batches from data with shape {data.shape}")

    examples = len(data)
    max_examples = examples - lookback * input_steps + 1 - forecast_step - forecast_len + 1
    if max_examples <= 0:
        raise ValueError(f"No examples generated from data of shape {data.shape} with lookback {lookback}, input_steps {input_steps}, forecast_step {forecast_step}, forecast_len {forecast_len}")

    x = np.empty((max_examples, lookback, num_inputs), dtype=np.float32)
    y = np.empty((max_examples, forecast_len, num_outputs), dtype=np.float32)

    for i in range(max_examples):
        x_start_idx = i
        x_end_idx = x_start_idx + lookback * input_steps
        y_start_idx = x_end_idx + forecast_step - input_steps
        y_end_idx = y_start_idx + forecast_len

        x[i] = data[x_start_idx:x_end_idx:input_steps, :num_inputs]
        y[i] = data[y_start_idx:y_end_idx, -num_outputs:]

    y = np.transpose(y, (0, 2, 1)).astype(np.float32)

    return x, y

# %%

@jit(nbTuple((float32[:, :, :], float32[:, :, :]))(float32[:, :], int32, int32, int32, int32, int32, int32), nopython=True, parallel=True)
def prepare_data3(
        data: np.ndarray,
        lookback: int,
        num_inputs: int,
        num_outputs: int,
        input_steps: int,
        forecast_step: int,
        forecast_len: int,
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Prepare input and output data for time series forecasting.
    """
    features = data.shape[1]

    if num_inputs + num_outputs != features:
        raise ValueError(f"num_inputs {num_inputs} + num_outputs {num_outputs} != total features {features}")

    if len(data) <= 1:
        raise ValueError(f"Cannot create batches from data with shape {data.shape}")

    examples = len(data)
    max_examples = examples - lookback * input_steps + 1 - forecast_step - forecast_len + 1
    if max_examples <= 0:
        raise ValueError(f"No examples generated from data of shape {data.shape} with lookback {lookback}, input_steps {input_steps}, forecast_step {forecast_step}, forecast_len {forecast_len}")

    x = np.empty((max_examples, lookback, num_inputs), dtype=np.float32)
    y = np.empty((max_examples, forecast_len, num_outputs), dtype=np.float32)

    for i in prange(max_examples):
        x_start_idx = i
        x_end_idx = x_start_idx + lookback * input_steps
        y_start_idx = x_end_idx + forecast_step - input_steps
        y_end_idx = y_start_idx + forecast_len

        x[i] = data[x_start_idx:x_end_idx:input_steps, :num_inputs]
        y[i] = data[y_start_idx:y_end_idx, -num_outputs:]

    y = np.transpose(y, (0, 2, 1)).astype(np.float32)

    return x, y


# %%

data = np.random.rand(5000, 6).astype(np.float32)  # Dummy data
lookback = 365
num_inputs = 5
num_outputs = 1
N = 1000

# %%
start = time.time()
for i in range(N):
    x, y = prepare_data(data, np.int32(lookback), num_inputs, num_outputs, np.int32(1), np.int32(0), np.int32(1))

print("Time taken :", time.time()-start)

# %%

start = time.time()
for i in range(N):
    x, y = prepare_data1(data, np.int32(lookback), num_inputs, num_outputs, np.int32(1), np.int32(0), np.int32(1))
print("Time taken with simple numba:", time.time()-start)

# %%

start = time.time()
for i in range(N):
    x, y = prepare_data2(data, np.int32(lookback), np.int32(num_inputs), np.int32(num_outputs), np.int32(1), np.int32(0), np.int32(1))
print("Time taken type annotation with numba:", time.time()-start)

# %%

start = time.time()
for i in range(N):
    x, y = prepare_data3(data, lookback, num_inputs, num_outputs, np.int32(1), np.int32(0), np.int32(1))
print("Time taken using prange in numba:", time.time()-start)