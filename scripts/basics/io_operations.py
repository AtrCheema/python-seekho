"""
===========================
1.17 read/write operations
===========================

This lesson shows how to read/write files using python.
"""

#############################
# creating new file
# -------------------
# If we want to create a new file we can make use of ``open`` function. The
# second argument here ``w`` defines that we would like to create a new file.

open("NewFile.txt", "w")

# %%
# The first argument to ``open`` must be complete path of the file. If only
# file name is given, it means the file will be created at current working directory.

#####################################
# The ``open`` function returns a file handler which can be useful.
new_file = open("NewFile.txt", "w")
print(type(new_file))

#####################################
# Using the file handler, we can check whether a file is open or closed.
# if a file is open, we can write in it. If it is closed, we can not.

print(new_file.closed)

#####################################
# We must close the file once we are done working with a file.

new_file.close()

print(new_file.closed)

#####################################
# Instead of manually closing the file everytime, we can automatically close it
# using ``with`` keyword. ``with`` is called context manager which makes sure that
# whenever we are out of it, the file is closed.

with open("NewFile.txt", "w") as fp:
    pass

print(fp.closed)

# %%
# Even if there is an error during writing/reading the file,
# the context manager makes sure that the file is closed despite the error.

# uncomment following lines
# with open("NewFile.txt", 'w') as fp:
#     fp.write("Bajwa chor hai")
#     raise NotImplementedError(f"You are not allowed to utter this.")

# %%
# If we uncomment and run the above cell, it will result in error but we can confirm that
# the file is still closed. We can verify this using following statement
print(fp.closed)  # --> True

##############################
# writing to a new file
# ----------------------
# If we want to write to a new file, we can make use of ``open`` function but
# with ``w`` as second argument.
#
# Context manager also returns us a file handler which can be used to
# read/write the file

with open("NewFile.txt", "w") as fp:
    fp.write("My Name is Ali")

##############################
# Here, ``fp`` is file handler, which can can use to modify file.
#
# The ``write`` function is for writing a string. If we want to write a list
# of strings, we can make use of ``writelines`` function.

lines = ['His name was Ali', 'He was very brave']

with open("NewFile.txt", "w") as fp:
    fp.writelines(lines)

# %%
# If we write something to an existing file and open the file
# with ``w``, the previous file will be overwritten. This can also cause
# loss of data.

new_lines = ['His name was Hussain.\n', 'He was very brave\n']

with open("NewFile.txt", "w") as fp:
    fp.writelines(new_lines)

# %%
# If we see the `NewFile.txt` we will see that it has `new_lines` and not
# `lines. This is because the previous file was deleted altogether.

##############################
# writing to already existing file
# ----------------------------------
# If want to write to an already existing file, the second argument to ``open``
# function must be ``a``

lines = ['He was killed in 661']

with open("NewFile.txt", "a") as fp:
    fp.writelines(lines)

##############################
# writing with specific separator
# ---------------------------------
# Consider that we want to write following data into a file.
lines = ["1 2 3", "1 2 3", "1 2 3"]

# %%
# We can do this using following lines of code.

# %%
with open("NewFile", 'w') as fp:
    for line in lines:
        line = ','.join(line.split())
        fp.write(line + '\n')

# %%
# Even though we have not defined the extension of file i.e., the file name
# is `NewFile`, but this file is still a text file which can be opened by
# any text editor.
# Above we used comma ``,`` to separate each value in a line. However, we can
# use any other separator that we wish e.g. a tab.

with open("NewFile", 'w') as fp:
    for line in lines:
        line = '\t'.join(line.split())
        fp.write(line + '\n')

##############################
# reading a file
# -------------------
# If we want to read a file, the second argument to ``open`` function must be
# ``r``. However, the file must exist at the location which is specified.

text = """Nb  C  O Cr 
 1.0
     9.461699    0.0    0.0
     0.590249    0.31933   29.99
 Nb  C   O   Cr 
  18   9  18   1
Cartesian
  0.13  1.87 11.074
 -1.44  4.60 11.076
 -3.02  7.33 11.075
  3.28  1.85 11.040"""

with open('NewFile', 'w') as fp:
    fp.write(text)

lines = []
with open('NewFile', 'r') as fp:
    for line_num, line in enumerate(fp.readlines()):
        if line_num > 6:
            line = line.split()  # split the line based upon spaces and put all members into a list
            lines.append([float(num) for num in line])

print(lines)

# %%
# We are using ``readlines`` function for reading all the lines lin the file.
# The ``readlines()`` actually returns us a ``list`` on which we can iterate. Then
# we are iterating over these lines one by one. Next we are saving the lines in `lines`
# list after line number 7.  Above the first argument is only file name. This means that the file must exists
# in current folder (working directory).

##############################
# reading large files
# ----------------------
# The problem with above methodology is that it reads all the lines into memory.
# If however, the file is large (in GigaBytes), we may not wish to read whole file
# into memory. In that case we can read line by line.

with open('NewFile', 'r') as fp:
    for idx, line in enumerate(fp):
        pass

# %%
# At every iteration, the previous ``line`` from memory is overwritten
# by the new ``line``.


##############################
# writing to a specific line
# ---------------------------
# If we want to write to a specific line in a file or modify a specific line in a file,
# we can achieve this by reading the whole lines and then adding/changing those
# specific lines and then writing the modified lines back to the same file.

with open('NewFile', 'r') as fp:
    lines = fp.readlines()

lines.insert(9, '1.111 2.2222 3.33333\n')  # 9 means line number 10

with open('NewFile', 'w') as fp:
    fp.writelines(lines)

##############################
# writing json format
# ---------------------
# `json` is a human readable file format. This file format is similar to python
# dictionary.

import json

data = {"name": "Ali", "age": 63, 'is_bold': True}

with open("NewFile.json", "w") as fp:
    json.dump(data, fp)

# %%
# The data that we wrote above, was a dictionary but we can write any other
# data to json file as far as it is of native python type.

with open("NewFile.json", "w") as fp:
    json.dump([1, 2, 3], fp)

##############################
# By setting the ``indent`` keyword argument, we can make sure that all the data
# is not saved on a single line. This makes the json file more readable.

with open("NewFile.json", "w") as fp:
    json.dump(data, fp, indent=True)

##############################
# We can sort the keys of saved dictionary in json file by setting ``sort_keys`` to True.

with open("NewFile.json", "w") as fp:
    json.dump(data, fp, indent=True, sort_keys=True)

##############################
# However, the json file can save only native python types. If the data
# is not native python type, we get the ``TypeError``

import numpy as np

np_data = np.array([2])

# uncomment following two lines, they will return in TypeError
# with open("jsonfile.json", "w") as fp:
#     json.dump(np_data, fp)  # -> TypeError: Object of type ndarray is not JSON serializable

# %%
# The error message very explicit says that the data we are trying to save
# is `ndarray <https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html>`_
# and it can not be `serialized <https://docs.python-guide.org/scenarios/serialization/>`_ .

##############################
# We can verify this by checking the type of `data`.

print(type(np_data))

##############################
# `data` is an array, which means it consists of multiple values.
# We can get the first value of `data` by slicing it using slice operator ``[]``.

np_data_0 = np_data[0]

print(np_data_0)

# %%
# Now If we try to save it in json file,

# Uncomment following two lines, they will result in TypeError
# with open("jsonfile.json", "w") as fp:
#    json.dump(np_data_0, fp)  # -> TypeError: Object of type int32 is not JSON serializable

##############################
# The above error message says that ``int32`` is also not serializable. This is
# because the first member of ``data`` is ``int32`` type which is from numpy library.

print(type(np_data_0))

##############################
# This is because ``int32`` is also not python's native type but is from numpy library.
#
# We can convert ``int32`` into python's ``int`` type and then we can save it into
# json file format.

np_data_0_int = int(np_data_0)

print(type(np_data_0_int))
# %%

with open("NewFile.json", "w") as fp:
    json.dump(np_data_0_int, fp)

##############################

np_data = np.array([2, 3, 4])

# Uncomment following two lines, they will result in TypeError
# with open("jsonfile.json", "w") as fp:
#     json.dump(np_data, fp)

##############################
# The ``tolist`` method of numpy array converts the numpy array into list
# which is python native type and can be saved as json.

data_list = np_data.tolist()

with open("NewFile.json", "w") as fp:
    json.dump(data_list, fp)

##############################
# reading json format
# ---------------------
# In order to read the json file, we can make use of ``json.load()`` function.
# The first argument must be file path.

with open("NewFile.json", "r") as fp:
    data = json.load(fp)

print(data)

# %%
# The type of the data is preserved when we load the json file.

print(type(data))

##############################
# writing in binary format
# -------------------------
# Above when we wrote the data, the saved file was human readable. This means
# that you can open the file and see/read the data. However, there is a cost of doing this.
# If the data is large, the file size gets extremely large and the process of reading
# and writing becomes slow. This can be avoided by writing the data into binary format.
# The downside here is that the written file is not human readable unless you have specific
# software e.g `HDFView <https://www.hdfgroup.org/downloads/hdfview/>`_ .
# These software actually convert the binary data into human readable and show it.
# Saving the data into binary format is a very large topic and there are many
# built-in and third-party libraries in python for it. However, here we will only cover
# basics of ``pickle`` module of python.

import pickle

# %%
# When we want to save the data into binary format/file, the second argument
# to ``open`` function must be ``wb``. Here, ``w`` means that we are creating
# a new file and ``b`` represents that the data will be written in binary format.

my_bytes = [120, 3, 255, 0, 1000]
with open("NewFile", "wb") as my_pickle_file:
    pickle.dump(my_bytes, my_pickle_file)

# %%
# Above all the elements in list were integer, however they can also be float

my_bytes = [120, 3, 255, 0, 1000.0]
with open("NewFile", "wb") as my_pickle_file:
    pickle.dump(my_bytes, my_pickle_file)

# %%
# also string data can be saved as binary using pickle module.

my_bytes = [120, 3, 255, 0, 1000.0, 'a']
with open("NewFile", "wb") as my_pickle_file:
    pickle.dump(my_bytes, my_pickle_file)

# %%
# Similarly we can write ``tuple`` or ``dictionary`` data into binary format.

my_bytes = [120, 3, 255, 0, 1000.0, 'a', (1, 2), None]
with open("NewFile", "wb") as my_pickle_file:
    pickle.dump(my_bytes, my_pickle_file)

# %%

my_bytes = [-1200, 3, 255, 0, 1000.0, 'a', {'a': 1}, True]
with open("NewFile", "wb") as my_pickle_file:
    pickle.dump(my_bytes, my_pickle_file)

##############################
# reading binary format
# -----------------------
# If we want to read binary file, we can use ``rb`` keyword in ``open``
# function as second argument.

with open("NewFile", "rb") as my_pickle_file:
    my_bytes = pickle.load(my_pickle_file)

print(my_bytes)

# %%
# The pickle module can read/write a wide range of data types.

my_bytes = np.array([120, 3, 255, 0, 1000.0])
with open("NewFile", "wb") as my_pickle_file:
    pickle.dump(my_bytes, my_pickle_file)

with open("NewFile", "rb") as my_pickle_file:
    my_bytes = pickle.load(my_pickle_file)

print(type(my_bytes))

# %%
# Above we wrote numpy data type which is not python's native data type.
# Moreover, when we read binary file, we still got numpy data type.
