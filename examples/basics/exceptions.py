"""
==================
1.18 Exceptions
==================
This lesson shows the usage of Exceptions in python
"""

# sphinx_gallery_line_numbers = True

import os

#%%
# An exception is basically an error which is raised when a statement or command
# fails in python.

a = 2

assert isinstance(a, int)

#%%
# The above statement did not return anything because the assertion was successful
# However if the assertion fails, we get a special kind of error called ``AssertionError``


#%%
# AssertionError
#===================

# uncomment following 1 line
# assert isinstance(a, float)

#%%
# Similar to AssertionError, there are many other types of errors/exceptions in python

##########################
# TypeError
#===================
# This error is raised when an operation is failed due to wrong type of a variable.

# uncomment following line
# 4 + 'a'

###################################
# ModuleNotFoundError
#=====================
# This error is raised when a specific module that we are importing is not **available/installed**.
# Whenever we import a variable, function or class or any python object, python
# searches in all the directories(folders) which are in its ``path``. So when we say
# a package is not installed or available, it means, this package or the object that we
# are importing is not avaialable in any of the directories in the path. In other words
# we also say that, this package/object is not available in python's path. If we want to
# check what are the lists of directories/folders in python's path, we can do this
# by printing the value of ``sys.path``.

#%%
# sys.path returns a ``list`` so we can iterate over it.

import sys

for p in sys.path:
    print(p)

#%%

# uncomment following 1 line
# import tensorflow as tf

#%%
# Since ``tensorflow`` package is not installed, we will get ModuleNotFoundError.

############################
# KeyError
#=============
# This error is raised when a specific key is not available in a dictionary

human = {"name": "Ali"}

# uncomment following 1 line
# print(human['age'])

################################
# PermissionError
#=================
# This error is raised when the user does not have permission to access the file
# or to do an operation on such a file for which he/she does not have rights.


f = open('NewFile.txt', 'w')

# uncomment the following line
# os.remove('NewFile.txt')  # -> PermissionError

#%%
# since the file ``NewFile.txt`` was already opened, we can not delete it
# and got ``PermissionError``

f.close()
os.remove('NewFile.txt')

#%%
# Once we close the file using ``f.close()``, then we can delete the file.

##############################
# FileNotFoundError
#=====================
# This error is raised when the the file that we are trying to open does not exist
# in the directory/path.

# uncomment following 1 line
# open("NonExistingFile", "r")

###########################
# Error handling
#=================
# So what is the purpose of knowing all of these errors?
#
# Sometimes we would like to forecast/predict an error and bypass
# the error by applying the solution.
#
# In the function below, we would like to add a value in 2. However
# if due to TypeError we can not do so, then we would first convert
# it to integer before adding it into ``2``.

def add_number(val):
    try:
        val = val+ 2
    except TypeError:
        print('TypeError was encountered but bypassed')
        val = int(val) + 2
    return val

add_number(2)

#%%
add_number('2')

#%%
# Error handling is also used by printing out more useful error messages to the user.
# Suppse the package ``tensorflow`` is not installed which may be required. Then instead
# of just throwing ``ModuleNotFoundError``, we can help the user by giving more helpful error message

def better_error_messgae():
    try:
        import tensorflow
    except ModuleNotFoundError as e:
        raise ModuleNotFoundError(f"You must install tensorflow using pip install tensorflow \n{e}")
    return

# uncomment following line
# better_error_messgae()

###########################
# Custom Errors
#=================
# We can create our own errors based upon our needs.
# Any new error must inherit from ``Exception`` class or its base classes.
#
# Below we create an error which will be raised if a value
# is above 256.

class IllegalValue(Exception):
    def __init__(self, val):
        self.val = val
    def __str__(self):
        return f"val must be below 256 but it is {self.val}"

value = 1000
#%%

# Uncomment collowing two lines
# if value>256:
#     raise IllegalValue(value)

#%% md
# Sometimes we want to handle/catch multiple exceptions, we can do this in one
# line by wrting all the exceptions inside a tuple after ``except``.

def multiple_exceptions(wname):
    try:
        out = float(wname.split('_')[2])
    except (ValueError, IndexError) as e:
        raise Exception(f"{wname} raised ", e)
    return out

#%%
# Above, we want to catch ValueError and IndexErro at the same time.

# uncomment following line
# multiple_exceptions("11_2.5.h5")  # -> IndexError

#%%

# uncomment following line
# multiple_exceptions("11_2_5.h5")  # -> ValueError

#%%

multiple_exceptions("11_2_5")