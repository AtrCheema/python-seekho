"""
==================
17. input/output
==================
This lesson shows how to read/write files using python.
"""

#############################
# creating new file
# -------------------
# If we want to create a new file we can make use of ``open`` function. The
# second argument here ``w`` defines that we would like to create a new file.

open("NewFile.txt", "w")

#%%
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
# using the context manager ``with``. Context manager ``with`` makes sure that
# whenever we are out of it, the file is closed.

with open("NewFile.txt", "w") as fp:
    pass

print(fp.closed)

# %%
# Even if there is an error during writing/reading the file
# the context manager makes sure that the file is closed after the error.

##############################
# writing to a new file
# ----------------------
# Context mangaer also returns us a file handler which can be used to
# read/write the file

with open("NewFile.txt", "w") as fp:
    fp.write("My Name is Ali")

##############################
# The ``write`` function is for writing a string. If we want to write a list
# of strings, we can make use of ``writelines`` function.

lines = ['His name was Ali', 'He was very brave']

with open("NewFile.txt", "w") as fp:
    fp.writelines(lines)

# %%
# If we write something to an existing file and open the file
# with ``w``, the file will be overwritten. This can also cause
# loss of data.

lines = ['His name was Ali.\n', 'He was very brave\n']

with open("NewFile.txt", "w") as fp:
    fp.writelines(lines)

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
lines = ["1 2 3", "1 2 3", "1 2 3"]
with open("NewFile", 'w') as fp:
    for line in lines:
        line = ','.join(line.split())
        fp.write(line + '\n')

# %%
# Above we used comma ``,`` to separateeach value in a line. However, we can
# use any other separator that we wish e.g. a tab.

with open("NewFile", 'w') as fp:
    for line in lines:
        line = '\t'.join(line.split())
        fp.write(line + '\n')

##############################
# reading a file
# -------------------
# If we want to read a file, the second argument to ``open`` function must be
# ``r``. However, the file must exist.

text = """Nb  C  O Cr 
 1.0000000000000000
     9.4616994858000005    0.0000000000000000    0.0000000000000000
     0.5902497990000000    0.3193300853000000   29.9935537031999999
 Nb  C   O   Cr 
  18   9  18   1
Cartesian
  0.1336766064210279  1.8753905438790981 11.0741757477844533
 -1.4468814995438639  4.6046320601937234 11.0765284421369312
 -3.0240037164799349  7.3362104723597765 11.0754772280667435
  3.2848511988924094  1.8556784559463604 11.0401360036995833"""

with open('NewFile', 'w') as fp:
    fp.write(text)

lines = []
with open('NewFile', 'r') as fp:
    for idx, line in enumerate(fp.readlines()):
        if idx > 7:
            line = ' '.join(line.split()).split(' ')
            lines.append([float(num) for num in line])

##############################
# reading large files
# ----------------------
# The problem with above methodology is that it reads all the lines into memory.
# If however, the file is large (in GBs), we may not wish to read whole file
# into memory. In that case we can read line by line.

with open('NewFile', 'r') as fp:
    for idx, line in enumerate(fp):
        pass

#%%
# At every iteration, the previous ``line`` from memory is overwritten
# by the new ``line``.


##############################
# writing to a specific line
# ---------------------------
# If we want to write to a specific line in a file or modify a specific line in a file,
# we can acheive this by reading the whole lines and then adding/changing those
# spefic lines and then writing the modified lines back to the same file.

with open('NewFile', 'r') as fp:
    lines = fp.readlines()

lines.insert(9, '1.111 2.2222 3.33333\n')

with open('NewFile', 'w') as fp:
    fp.writelines(lines)

##############################
# writing binary format
# ----------------------
# When we wrote data above, the saved data was human readable. This means
# that you can open the file and see/read the data. However, there is cost of doing this.
# If the data is large, the file size gets extremely large and the process of reading
# and writing becomes slow. This can be avoided by writing the data into binary format.
# The downside here is that the written file is not human readable unless you have specific
# softwares. These softwares actually convert the binary data into human readable and show it.
# Saving the data into binary format is a very large topic and there are many
# built-in and third-party libraries in python for it. However, here we will cover
# only basics of ``pickle`` module of python.

import pickle

#%%
# When we want to save the data into binary format/file, the second argument
# to ``open`` function must be ``wb``. Here, ``w`` stands for writing.

mybytes = [120, 3, 255, 0, 1000]
with open("NewFile", "wb") as mypicklefile:
    pickle.dump(mybytes, mypicklefile)

# %%
# Above all the elements in list were integer, however they can also be float

mybytes = [120, 3, 255, 0, 1000.0]
with open("NewFile", "wb") as mypicklefile:
    pickle.dump(mybytes, mypicklefile)

# %%
# also string data can be saved as binary using pickle.

mybytes = [120, 3, 255, 0, 1000.0, 'a']
with open("NewFile", "wb") as mypicklefile:
    pickle.dump(mybytes, mypicklefile)

# %%

mybytes = [120, 3, 255, 0, 1000.0, 'a', (1,2), None]
with open("NewFile", "wb") as mypicklefile:
    pickle.dump(mybytes, mypicklefile)

# %%

mybytes = [-1200, 3, 255, 0, 1000.0, 'a', {'a': 1}, True]
with open("NewFile", "wb") as mypicklefile:
    pickle.dump(mybytes, mypicklefile)

##############################
# reading binary format
# -----------------------
# for reading binary file we will use ``rb``

with open("NewFile", "rb") as mypicklefile:
    mybytes = pickle.load(mypicklefile)

print(mybytes)

#%%
# The pickle module covers a wide range of types
import numpy as np

mybytes = np.array([120, 3, 255, 0, 1000.0])
with open("NewFile", "wb") as mypicklefile:
    pickle.dump(mybytes, mypicklefile)

with open("NewFile", "rb") as mypicklefile:
    mybytes = pickle.load(mypicklefile)

print(type(mybytes))

##############################
# writing json format
# ---------------------
# `json` is a human readable file format. This file format is similar to python
# dictionary.

import json

data = {"name": "Ali", "age": 63, 'is_bold': True}

with open("NewFile.json", "w") as fp:
    json.dump(data, fp)

##############################
# By setting the ``indent`` keyword argument, we can make sure that all the data
# is not saved on a single line and it is more readable.

with open("NewFile.json", "w") as fp:
    json.dump(data, fp, indent=True)

##############################
# We can sort the keys of saved dictionary in json by setting ``sort_keys`` to True.

with open("NewFile.json", "w") as fp:
    json.dump(data, fp, indent=True, sort_keys=True)

##############################
# However, the json file can save only native python types. If the data
# is not native python type, we get the TypeError

import numpy as np

data = np.array([2])

# uncomment following two lines, they will return in TypeError
# with open("jsonfile.json", "w") as fp:
#     json.dump(data, fp)  # -> TypeError: Object of type ndarray is not JSON serializable

#%%
# The error message very explicity says that the data we are trying to save
# is ``ndarray`` and it can not be serialized.

##############################
# We can verify this by checking the type of ``data``.

print(type(data))

##############################

data_0 = data[0]

# Uncomment following two lines, they will result in TypeError
# with open("jsonfile.json", "w") as fp:
#    json.dump(data_0, fp)  # -> TypeError: Object of type int32 is not JSON serializable

##############################
# The above error message says that ``int32`` is also not serializable.

print(type(data_0))

##############################
# This is because ``int32`` is not python's native type but is from numpy library.
#
# We can convert ``int32`` into python's ``int`` type and then we can save it into
# json file format.

data_0 = int(data_0)

print(type(data_0))
#%%

with open("NewFile.json", "w") as fp:
    json.dump(data_0, fp)

##############################

data = np.array([2, 3, 4])

# Uncomment following two lines, they will result in TypeError
# with open("jsonfile.json", "w") as fp:
#     json.dump(data, fp)

##############################
# The ``tolist`` method of numpy array converts the numpy array into list
# which is python native type and can be saved as json

data_list = data.tolist()

with open("NewFile.json", "w") as fp:
    json.dump(data_list, fp)

##############################
# reading json format
# ---------------------
# In order to read the json file, we can make use of ``json.load()`` function.
# The first arguemnt must by file handle

with open("NewFile.json", "r") as fp:
    data = json.load(fp)

print(data)

# %%
# The type of the data is preserved when we load the json file

print(type(data))

#%%
# finding files
#---------------

for i in range(5):
    with open(f'TextFile_{i}.txt', 'w'):
        pass
for i in range(5):
    with open(f'CsvFile_{i}.csv', 'w'):
        pass

#%%
# If we want to find all files and folders within a specific path

import os

path_to_look = os.getcwd()

print(os.listdir(path_to_look))

#%%
# If want to find only files and not folders/directories, we can do following
# list comprehension.

print([f for f in os.listdir(path_to_look) if os.path.isfile(f)])

#%%
# If we want to find files with a specific extension, we can do as following

print([f for f in os.listdir(path_to_look) if os.path.isfile(f) and f.endswith(".txt")])

#%%
# If we want to find files with a specific extension, and starting with a
# specific name, we can do as following
print([f for f in os.listdir(path_to_look) if os.path.isfile(f) and f.endswith(".txt") and f.startswith('TextFile_')])
