"""
============================
7.5 interfacing with C++
============================

This lesson describes how to call functions/modules written in C++ into python and
"""



# import ctypes
# import subprocess
# from ctypes import c_char_p, c_uint, c_size_t, POINTER, Structure

# import numpy as np
# import pandas as pd

# # Specify the C++ source file and the output executable name
# cpp_source_file = 'read_csv_gpt.cpp'
# output_library = 'read_csv_gpt.so'

# # Compile the C++ code as a library
# compile_command = f'g++ -shared -o {output_library}  -fPIC {cpp_source_file}'
# subprocess.run(compile_command, shell=True)

# # Define the CSVRow structure
# class CSVRow(Structure):
    
#     _fields_ = [("date", ctypes.c_char * 20),
#                 ("floatValue", ctypes.c_float)]

# # Load the shared library
# csv_reader = ctypes.CDLL(f'./{output_library}')  # Use the correct path for your .so/.dll file

# # Define the argument and return types of the functions
# csv_reader.processCSVFile.argtypes = [c_char_p, POINTER(c_uint), POINTER(c_size_t)]
# csv_reader.processCSVFile.restype = POINTER(CSVRow)

# csv_reader.freeCSVRows.argtypes = [POINTER(CSVRow)]
# csv_reader.freeCSVRows.restype = None

# def read_csv(file_path):
#     # Call the processCSVFile function
#     station = c_uint(0)
#     size = c_size_t(0)
#     rows = csv_reader.processCSVFile(file_path, ctypes.byref(station), ctypes.byref(size))

#     # Access the returned data
#     data = [None] * size.value
#     index = [None] * size.value
#     for i in range(size.value):
#         index[i] = rows[i].date.decode('utf-8')
#         data[i] = rows[i].floatValue

#     df = pd.DataFrame(data, columns=[str(station.value)], index=index)
#     df.replace(-9999.0, np.nan, inplace=True)

#     # Free the allocated memory
#     csv_reader.freeCSVRows(rows)

#     return df

# df = read_csv(b'daily_q.csv')

# import time
# start = time.time()
# for i in range(50):
#     read_csv(b'daily_q.csv')

# print(f"Time taken to read the CSV file 5 times: {time.time() - start:.2f} seconds")


# start = time.time()
# for i in range(50):
#     df1 = pd.read_csv('daily_q.csv', index_col=0)
# print(f"Time taken to read the CSV file 5 times: {time.time() - start:.2f} seconds")


# %%

import time
import ctypes
import pandas as pd
import numpy as np
import subprocess


# Specify the C++ source file and the output executable name
cpp_source_file = 'read_csv_gpt.cpp'
output_library = 'read_csv_gpt.so'

# Compile the C++ code as a library
compile_command = f'g++ -shared -o {output_library}  -fPIC {cpp_source_file}'
subprocess.run(compile_command, shell=True)

# Define the CSVRow structure
class CSVRow(ctypes.Structure):
    _fields_ = [("date", ctypes.c_char * 20),
                ("floatValue", ctypes.c_float)]

# Load the shared library
csv_reader = ctypes.CDLL(f'./{output_library}')   # Use the correct path for your .so/.dll file

# Define the argument and return types of the functions
csv_reader.processCSVFileFast.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_uint), ctypes.POINTER(ctypes.c_size_t), ctypes.POINTER(ctypes.c_size_t)]
csv_reader.processCSVFile.restype = ctypes.c_void_p

csv_reader.freeCSVRowsFast.argtypes = [ctypes.c_void_p]
csv_reader.freeCSVRowsFast.restype = None


def read_csvFast(file_path):
    # Call the processCSVFileFast function
    total = ctypes.c_uint(0)
    size = ctypes.c_size_t(0)
    row_size = ctypes.c_size_t(0)
    ptr = csv_reader.processCSVFileFast(file_path, ctypes.byref(total), ctypes.byref(size), ctypes.byref(row_size))

    # # Check if the pointer is NULL
    # if not ptr:
    #     raise MemoryError("Failed to allocate memory for CSV data")

    # Convert the pointer to a numpy array
    buffer = (ctypes.c_char * (size.value * row_size.value)).from_address(ptr)
    data = np.frombuffer(buffer, dtype=[('date', 'S20'), (str(total.value), 'f4')])

    # Create a pandas DataFrame from the numpy array
    df = pd.DataFrame(data)

    # Convert the 'date' column to string
    df.index = df['date'].str.decode('utf-8')

    # Free the allocated memory
    csv_reader.freeCSVRowsFast(ptr)
    return df

start = time.time()
for i in range(50):
    df = read_csvFast(b'daily_q.csv')

print(f"Time taken to read the CSV file 5 times: {time.time() - start:.2f} seconds")