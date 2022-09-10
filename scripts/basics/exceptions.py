"""
==================
1.18 Exceptions
==================
This lesson shows the usage of exceptions in python
"""

# %%
# An exception is basically an error which is raised when a statement or command
# fails in python.

a = 2

assert isinstance(a, int)

# %%
# The function ``isinstance`` is being used here to check the ``type`` of a python object.
# The above statement did not return anything because the assertion was successful.
# However if the assertion fails, we get a special kind of error called ``AssertionError``.


# %%
# AssertionError
# ---------------
# If we run the code given below, it will result in ``AssertionError`` because
#  the variable `a` is ``int`` type and not ``float`` type.

# uncomment following 1 line
# assert isinstance(a, float)

# %%
# We can write more useful error messages instead of throwing just ``AssertionError`` as follows,

# uncomment following 1 line
# assert isinstance(a, float), f"a is not float but is of {type(float)} type"

# %%
# Similar to ``AssertionError``, there are many other types of errors/exceptions in python

# %%
# TypeError
# -----------
# This error is raised when an operation is failed due to wrong ``type`` of a variable.

# uncomment following line
# 4 + 'a'  # -> TypeError: unsupported operand type(s) for +: 'int' and 'str'

# %%
# Since we can not add a string into an integer, we got ``TypeError`` above.

# %%
# ModuleNotFoundError
# ---------------------
# This error is raised when a specific module that we are importing is not **available/installed**.

# %%

# uncomment following 1 line
# import ai4water as tf  # -> ModuleNotFoundError: No module named 'ai4water'

# %%
# Since ``ai4water`` package is not installed, we got ``ModuleNotFoundError`` above.
#
# Whenever we import a variable, function or class or any python object, python
# searches in all the directories (folders) which are in its ``path``. So when we say
# a package is not installed or available, it means, this package or the object that we
# are importing is not available in any of the directories in the ``path``. In other words
# we also say that, this package/object is not available in python's path. If we want to
# check what are the lists of directories/folders in python's path, we can do this
# by printing the value of ``sys.path``.

# %%
# sys.path returns a ``list`` so we can iterate over it.

import sys

for p in sys.path:
    print(p)

############################
# KeyError
# -----------
# This error is raised when a specific key is not available in a dictionary.

human = {"name": "Ali"}

# uncomment following 1 line
# print(human['age'])  # KeyError: 'age'

# %%
# Since the dictionary `human` does not have `age` key, we will get ``KeyError``,
# if we will run the above cell.

################################
# PermissionError
# ----------------
# This error is raised when the user does not have permission to access the file
# or to do an operation on such a file for which he/she does not have corresponding rights.


f = open('NewFile.txt', 'w')

import os

# uncomment the following line
# os.remove('NewFile.txt')  # -> PermissionError

# %%
# since the file `NewFile.txt` was already opened, we can not delete it
# and got ``PermissionError``.

f.close()
os.remove('NewFile.txt')

# %%
# Once we close the file using ``f.close()``, then we can delete the file.

# %%
# ``PermissionError`` is also raised when you are trying to open/create a file
# but the first argument to ``open`` function is folder instead of file.


##############################
# FileNotFoundError
# ---------------------
# This error is raised when the the file that we are trying to open does not exist
# in the directory/path.

# uncomment following 1 line
# open("NonExistingFile", "r")  # -> FileNotFoundError: [Errno 2] No such file or directory: 'NonExistingFile'

# %%
# IndexError
# -----------
# This error is raised when try to access a value from a sequence based upon the index which
# is not available for that sequence. For example, for a list with three members, if we
# try to access its fourth member, we will get ``IndexError``.

my_list = [1, 2, 3]
# uncomment following line
# my_list[3]  # -> IndexError: list index out of range

# %%
# Same is true for tuples.

my_tuple = (1, 2, 3)

# uncomment following line
# my_tuple[3]  # -> IndexError: tuple index out of range

# %%
# There is another commonly encountered error i.e., ``AttributeError``. We are
# not introducing it here. It will discussed later in :ref:`sphx_glr_auto_examples_oop___getattr__.py`.

###########################
# Error handling
# ------------------
# So what is the purpose of knowing all of these errors?
#
# Sometimes we would like to forecast/predict an error and bypass
# the error by applying the solution.  In the function below, we would
# like to add a value in 2. However, if due to ``TypeError`` we can not
# do so, then we would first convert it to integer before adding it into 2.


def add_number(val):
    try:
        val = val + 2
    except TypeError:
        print('TypeError was encountered but bypassed')
        val = int(val) + 2
    return val


add_number(2)

# %%
add_number('2')

# %% md
# Sometimes we want to handle/catch multiple exceptions. We can do this in one
# line by writing all the exceptions inside a tuple after ``except`` keyword.


def multiple_exceptions(wname):
    try:
        out = float(wname.split('_')[2])
    except (ValueError, IndexError) as e:
        raise Exception(f"{wname} raised ", e)
    return out


# %%
# Above, we want to catch ValueError and IndexError at the same time.

# uncomment following line
# multiple_exceptions("11_2.5.h5")  # -> IndexError

# %%

# uncomment following line
# multiple_exceptions("11_2_5.h5")  # -> ValueError

# %%

multiple_exceptions("11_2_5")

# %%
# Error handling is also used by printing out more useful error messages to the user.
# Suppose the package ``ai4water`` is not installed which may be required. Then instead
# of just throwing ``ModuleNotFoundError``, we can help the user by giving more helpful error message


def better_error_message():
    try:
        import ai4water
    except ModuleNotFoundError as e:
        raise ModuleNotFoundError(f"You must install ai4water using pip install ai4water \n{e}")
    return

# uncomment following line
# better_error_message()

###########################
# Custom Errors
# -----------------
# We can create our own errors based upon our needs.
# Any new error must inherit from ``Exception`` class or its base classes.
# If at this stage you are uncomfortable with the concept of ``class`` or `base class`,
# you can jump to lessons of :ref:`sphx_glr_auto_examples_oop_introduction.py`
# and :ref:`sphx_glr_auto_examples_oop_inheritance.py` in :ref:`sphx_glr_auto_examples_oop`
# chapter to know about them.
#
# Below we create an error which will be raised if a value
# is above 256.


class IllegalValue(Exception):
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return f"val must be below 256 but it is {self.val}"


value = 1000
# %%
# We can invoke this as given below.

# Uncomment following two lines
# if value>256:
#     raise IllegalValue(value)
