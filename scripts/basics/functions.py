"""
=================
1.12 functions
=================
.. important::
  This lesson is still under development.

"""

# %% md
# A function is a box which takes something as input and it gives you output after
# performing some operations in that input. In python, the input and
# output arguments are optional. The basic syntax of a minimal function in is as
# below
#
# .. code-block:: python
#
#    def FunctionName(InputArguments):
#        commands to find output
#        return output
#
# As said earlier, `InputArguments` and ``return`` are optional.


# %%

def add_nums():
    pass


print(add_nums)

# %%

type(add_nums)

# %% md
# If we want to use/run the function, this means we want to **call** it.
# Following syntax can be used to call the function
#
# .. code-block:: python
#
#    Output = FunctionName(InputArguments)
#
#
# ``Output`` is optional and so does ``InputArguments``

# %%

add_nums()

# %% md
# The following function takes two input arguments and adds them

# %%


def add_nums(_a, _b):  # for brevity, we can not write add_nums(_a+_b):
    print('_a: ', _a, ' _b:', _b)
    _a + _b


add_nums(1, 5)

# %% md
# Inside the function, we name the two input arguments as `_a` and `_b`.

# %%


def add_nums(_a, _b):
    print('_a: ', _a, ' _b:', _b)
    _a + _b


x = 12
y = 14
add_nums(x, y)

# %% md
# Outside function ``12`` is ``x`` but inside function, ``12`` is ``_a``. The
# variable ``_a`` is not available outside function.

# %%


def add_nums(_a, _b):
    print('_a: ', _a, ' _b:', _b)
    c = _a + _b
    return c


x = 12
y = 14
add_nums(x, y)

# %% md
# Inside the function we created ``c`` and returned it. Outside the function when
# called the function, this value of ``c`` is printed the variable named ``c``
# is not available itself. We can assign this value to a new variable whose
# is is ``z`` below. It can be any legal variable name.
# Which variables can be seen inside the function and which can be seen outside
# the function will be covered under the topic global and local variables.

# %%


def add_nums(_a, _b):
    print('_a: ', _a, ' _b:', _b)
    c = _a + _b
    return c


x = 12
y = 14
z = add_nums(x, y)
print('The function returns z: ', z)

# %% md
# `c` and ``z`` have same values with the difference that `c` exists only inside
# the function. However, creation of `c` is not necessary, we can just return
# the result as it is.

# %%


def add_nums(_a, _b):
    print('_a: ', _a, ' _b:', _b)
    return _a + _b


x = 12
y = 14
z = add_nums(x, y)
print('The function returns z: ', z)

# %% md
# Default arguments can be provided to input arguments. The default arguments
# are only used if we don't provide their values when calling them, otherwise
# their values are overwritten.

# %%


def add_nums(_a=12, _b=14):
    print('_a: ', _a, ' _b:', _b)
    return _a + _b


x = 114
y = 313
z = add_nums(x, y)
print('The function returns z: ', z)

# %% md
# Above: The value from variable ``x`` is going to ``_a`` and will replace its
# default value. The value from variable `y` will go to ``_b`` and will
# overwrite its default value i.e. 14.
#
# When we have have defined the default values of input arguments in function
# definition, we can skip one or more input arguments when calling the function as shown below.

# %%


def add_nums(_a=12, _b=14):
    print('_a: ', _a, ' _b:', _b)
    return _a + _b


y = 313
z = add_nums(y)
print('The function returns z: ', z)

# %% md
# Above, the value from `y` will be assigned to `_a` while `_b` will use its default value.

# %%


def add_nums(_a=12, _b=14):
    print('_a: ', _a, ' _b:', _b)
    return _a + _b


y = 313
z = add_nums(_b=y)
print('The function returns z: ', z)

# %% md
# Above, `_a` will use its default value while `_b` will get value of `y`.

# %%


def add_nums(_a=12, _b=14):
    print('_a: ', _a, ' _b:', _b)
    return _a + _b


x = 114
z = add_nums(_a=x)
print('The function returns z: ', z)

# %% md
# Above: `_a` will use the value of `x` i.e. 114 while `_b` will use its
# default value i.e. 14.

# %%


def add_nums(_a=12, _b=14):
    print('_a: ', _a, ' _b:', _b)
    return _a + _b


z = add_nums(1)
print('The function returns z: ', z)

# %% md
# Above, `1` will go to `_a` while `_b` will use its default value.
# The function cal also be called without providing any input argument
# because both input arguments are optional. In this case the default values will be used.

# %%


def add_nums(_a=12, _b=14):
    print('_a: ', _a, ' _b:', _b)
    return _a + _b


z = add_nums()
print('The function returns z: ', z)

# %% md
# We can define the optional arguments with obligatory arguments. In function
# below, `_c` is optional, while `_a` and `_b` are obligatory.

# %%


def add_nums(_a, _b, _c=14):
    print('_a:', _a, '  _b:', _b, '  _c:', _c)
    return _a + _b


z = add_nums(1, 2)
print('The function returns z: ', z)

# %% md
# Above, we have not provided the value for `_c`. As it was optional argument,
# its default value was used.

# %% md
# What will be the output of following function?

# %%

# z = add_nums()
# print('The function returns z: ', z)

# %% md
# Guess the output from following cell.

# %%

# z = add_nums(a=1, c=313)
# print('The function returns z: ', z)

# %% md

# Return
# A function returns `None` by default.

# %%

import random
qatleen = ['winsten churchil', 'rana sanaullah', 'obama', 'musharaf']


def print_qatal():
    print(random.choice(qatleen))
    return None


a = print_qatal()
type(a)

# %% md
# Even if a function does not return anything explicitly, it returns `None`.

# %%


def print_qatal():
    print(random.choice(qatleen))
    return


a = print_qatal()
type(a)

# %% md
# if a function does not return anything, it returns `None`.

# %%


def print_qatal():
    print(random.choice(qatleen))


a = print_qatal()
type(a)

# %% md
# So it is impossible in python to write a function which returns absolutely nothing.

# %%


def func(a, b):
    x = a
    y = b
    return x, y


xx = func(5, 12)
print(xx, type(xx))

# %% md
# Above: The function returns 2 arguments but we assigned it to 1 variable
# named `xx`. Thus, `xx` will be a tuple consisting of two values

# %%

xx, yy = func(5, 12)
print(xx, type(xx))
print(yy, type(yy))

# %% md
# If the function returns fewer arguments that the variables assigned, then it
# will give error. Try calling `xx, yy, zz = func(5,12)` and it will give error.

# %% md
# If the function returns multiple values but we want to get only one value, we can do it as

# %%

xx = func(15, 12)[1]
print(xx)

# %% md

# return a tuple from function

# %%


def retun_list(a):
    return [a]

out = retun_list(10)
type(out)

# %%


def return_tuple(variable):
    return (variable, variable)


out = return_tuple(10)
type(out)

# %%


def return_tuple(variable):
    return (variable)


out = return_tuple(10)
type(out)

# %% md
# The reason is that it is comma `,` which makes something a tuple not the brackets.
# So in order to get a tuple from function, we must put comma event if
# there is only one object in the tuple as shown below.

# %%

def return_tuple(variable):
    return (variable, )


out = return_tuple(10)
type(out)

# %% md
# function as input argument
# ---------------------------

# We can assign a function to a variable and use that variable to call the function.

# %%


def print_me(to_print):
    print(to_print)


a = print_me

a('This goes into print_me')

# %% md
# Thus we can use functions as input arguments to other functions as well.

# %%


def magic(left, op, right):
    return op(left, right)


def my_op(var_a, var_b):
    return var_a == var_b


magic(2, my_op, 2)

# %% md
# break vs return
# ---------------

# %%


def add_nums(a_list, break_point=5):
    _sum = 0.0
    for val in a_list:
        _sum += val
        if _sum > break_point:
            break
    return _sum


a = add_nums([1, 2, 3, 4, 5])
print(a)

# %% md
# As soon as the value of `_sum` became greater than `break_point` the function
# exited and we got the value of _sum at that point.

# %%

a = add_nums([1, 2, 3, 4, 5], 50)
print(a)

# %% md
# Was the ``break`` statement executed above?

# %% md

# docstring
# The first string inside the functions is usually put for help. This is
# called `docstring`. It can be called by ``__doc__`` method

# %%


def fahrenheit(T_in_celcius):
    """This function converts temperature from Celsius to Fahrenheit. """
    return (T_in_celsius * 9 / 5) + 32

fahrenheit.__doc__

# %%

help(fahrenheit)

# %% md
# If we want to know the name of a function as string we can do it as following.

# %%

converter = fahrenheit

print(converter.__name__)
