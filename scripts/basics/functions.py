"""
=================
1.12 functions
=================
.. important::
  This lesson is still under development.

"""

# %% md
# A function is a box which takes something as input and it gives you output after
# performing some operations on that input. In python, the input and
# output arguments for a function are optional. The basic syntax of a minimal function in is as
# below
#
# .. code-block:: python
#
#    def FunctionName(InputArguments):
#        commands to find output
#        return output
#
# As said earlier, `InputArguments` and ``return`` are optional. This means we can write
# a valid function in python without input arguments or a function which does not
# return something.

# %%

def add_nums():
    pass

print(add_nums)

# %%

type(add_nums)

# %% md
# If we want to use/run a function, this means we want to **call** it.
# Following syntax can be used to call a function
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

def add_nums(a, b):  # for brevity, we can not write add_nums(a+b):
    print('a: ', a, ' b:', b)
    a + b

add_nums(1, 5)

# %% md
# Inside the function, we name the two input arguments as `a` and `b`.

# %%

def add_nums(a, b):
    print('a: ', a, ' b:', b)
    a + b

x = 12
y = 14
add_nums(x, y)

# %% md
# It is important to understant that the variable `a` and `b` are
# created once we are inside the function ``add_nums``.
#
# Outside function `12` is `x` but inside function, `12` is `a`. The
# variables `a` and `b` are not available outside the function.

# %%

def add_nums(a, b):
    print('a: ', a, ' b:', b)
    c = a + b
    return c

x = 12
y = 14
add_nums(x, y)

# %% md
# Above we we created `c` inside the function and returned it using the ``return`` statement. Outside the function when
# we `called` the function `add_nums` by executing ``add_nums(x,y)``, this value of `c` is printed. The variable named `c`
# itself is not available outside the function. 
# The variables which can be seen inside the function and which can be seen outside
# the function will be covered in :ref:`sphx_glr_auto_examples_basics_global_vs_local.py`.

# %%

# %% md
# Return
# -------
# A function returns ``None`` by default. The value returned by a function can 
# be assigned to a new variable for example to `x` in following example.
# It can be any legal variable name though.

# %%

import random  # ignore this line if you don't know what it does
qatleen = ['winsten churchil', 'rana sanaullah', 'obama', 'musharaf']

def print_qatal():
    print(random.choice(qatleen))
    return None

x = print_qatal()
print('type of x: ', type(x))

# %% md
# Even if a function does not return anything explicitly, it still returns ``None``.

# %%

def print_qatal():
    print(random.choice(qatleen))
    return


x = print_qatal()
print('type of x: ', type(x))

# %% md
# If a function does not have ``return`` statement, it still returns ``None``.

# %%

def print_qatal():
    print(random.choice(qatleen))

x = print_qatal()
print('type of x: ', type(x))

# %% md
# So it is impossible in python to write a function which returns absolutely nothing.

# %%

def add_nums(a, b):
    print('a: ', a, ' b:', b)
    c = a + b
    return c


x = 12
y = 14
z = add_nums(x, y)
print('The function returns z: ', z)

# %% md
# The variables `c` and `z` have same values with the difference that `c` exists only inside
# the function. Moreover, the creation of `c` is not necessary, we can just return
# the result as it is.

def add_nums(a, b):
    print('a: ', a, ' b:', b)
    return a + b  # no intermediate variable c

x = 12
y = 14
z = add_nums(x, y)
print('The function returns z: ', z)

# %%
# **Question**:
# What value will be printed as a result of code in following cell?
#
# .. code-block:: python
#
#    def add_nums(a, b):
#        print('a: ', a, ' b:', b)
#        z = a + b
#
#    x = 12
#    y = 14
#    z = add_nums(x, y)
#    print('The function returns z: ', z)

# %%
# **Question**:
# What value will be printed as a result of code in following cell?
#
# .. code-block:: python
#
#    def add_nums(a, b):
#        print('a: ', a, ' b:', b)
#        c = a + b
#
#    x = 12
#    y = 14
#    add_nums(x, y)
#    print('The value of c is: ', c)

# %%
# **Question**:
# What value will be printed as a result of code in following cell?
#
# .. code-block:: python
#
#    def add_nums(a, b):
#        print('a: ', a, ' b:', b)
#        c = a + b
#        return c
#
#    x = 12
#    y = 14
#    add_nums(x, y)
#    print('The value of c is: ', c)

# %%
# **Question**:
# What value will be printed as a result of code in following cell?
#
# .. code-block:: python
#
#    def add_nums(a, b):
#        print('a: ', a, ' b:', b)
#        c = a + b
#        return c
#
#    x = 12
#    y = 14
#    z = add_nums(x, y)
#    print('The value of c is: ', c)

# %%
# **Question**:
# What value will be printed as a result of code in following cell?
#
# .. code-block:: python
#
#    def add_nums(a, b):
#        print('a: ', a, ' b:', b)
#        c = a + b
#        return c
#
#    x = 12
#    y = 14
#    z = add_nums(x, y)
#    print('The value of z is: ', c)

# %% md
# Default values of input arguments
# ---------------------------------
# We can provide default values to input arguments. The default values of input arguments
# are only used if we don't provide their values when calling them, otherwise
# their values are overwritten.

# %%

def add_nums(a=12, b=14):
    print('a: ', a, ' b:', b)
    return a + b

x = 114
y = 313
z = add_nums(x, y)
print('The function returns z: ', z)

# %% md
# Above: The value from variable `x` is going to `a` and will replace its
# default value. The value from variable `y` will go to `b` and will
# overwrite its default value i.e. 14.
#
# When we have defined the default values of input arguments in function
# definition, we can skip one or more input arguments when calling the function as shown below.

# %%

def add_nums(a=12, b=14):
    print('a: ', a, ' b:', b)
    return a + b

y = 313
z = add_nums(y)
print('The function returns z: ', z)

# %% md
# Above, the value from `y` will be assigned to `a` while `b` will use its default value.

# %%

def add_nums(a=12, b=14):
    print('a: ', a, ' b:', b)
    return a + b

y = 313
z = add_nums(b=y)
print('The function returns z: ', z)

# %% md
# Above, `a` will use its default value while `b` will get value of `y`.

# %%


def add_nums(a=12, b=14):
    print('a: ', a, ' b:', b)
    return a + b

x = 114
z = add_nums(a=x)
print('The function returns z: ', z)

# %% md
# Above: `a` will use the value of `x` i.e. 114 while `b` will use its
# default value i.e. 14.

# %%

def add_nums(a=12, b=14):
    print('a: ', a, ' b:', b)
    return a + b

z = add_nums(1)
print('The function returns z: ', z)

# %% md
# Above, `1` will go to `a` while `b` will use its default value.
# The function can also be called without providing any input argument
# because both input arguments are optional. In this case the default values will be used.

# %%

def add_nums(a=12, b=14):
    print('a: ', a, ' b:', b)
    return a + b

z = add_nums()
print('The function returns z: ', z)

# %% md
# We can define the optional arguments with obligatory arguments. In function
# below, `c` is optional, while `a` and `b` are obligatory.

# %%

def add_nums(a, b, c=14):
    print('a:', a, '  b:', b, '  c:', c)
    return a + b

z = add_nums(1, 2)
print('The function returns z: ', z)

# %% md
# Above, we have not provided the value for `_c`. As it was optional argument,
# its default value was used.

# %% md
# **Question**:
# What will be the output of following function?

# %%
# .. code-block:: python
#
#    z = add_nums()
#    print('The function returns z: ', z)

# %% md
# **Question**:
# Guess the output from following cell.

# %%
# 
# .. code-block:: python
#
#    z = add_nums(a=1, c=313)
#     print('The function returns z: ', z)
#

# %%
# Returning multiple values
# -------------------------
# If a function returns more than one object/variables, and we assign it
# to a single variable, then this new variable will be ``tuple``.

def func(a, b):
    u = a
    v = b
    return u, v

xx = func(5, 12)
print(xx, type(xx))

# %% md
# Above: The function returns 2 arguments but we assigned it to 1 variable
# named `xx`. Thus, `xx` will be a tuple consisting of two values
#
# We can however, assign both returned values from a function to two new variables
# as shown below.
# %%

xx, yy = func(5, 12)
print(xx, type(xx))
print(yy, type(yy))

# %% md
# If the function returns fewer or more arguments than the variables assigned, then it
# will give error.

# %%

# uncomment the following line
# xx, yy, zz = func(5, 12)  # Error

# %% md
# If the function returns multiple values but we want to get only first value,
# we can do it as below

# %%

xx = func(15, 12)[1]
print(xx)

# %% md
# Above, we are slicing the output of `func` using `[1]` to get the second value.
# The type of the returned value will be the same as the type of the value returned by the function.

# %%

def retun_list(a):
    return [a]

out = retun_list(10)
print(type(out))

# %%
# A function can return a tuple in following ways

def return_tuple(variable):
    return variable, variable

out = return_tuple(10)
print(type(out))
# %%

def return_tuple(variable):
    return variable,

out = return_tuple(10)
print(type(out))
# %%

def return_tuple(variable):
    return (variable)

out = return_tuple(10)
print(type(out))

# %% md
# The type of `out` is ``int`` because it is comma ``,`` which makes something a tuple not the brackets.
# So in order to get a tuple from function, we must put comma even if
# there is only one object in the tuple as shown below.

# %%

def return_tuple(variable):
    return (variable, )

out = return_tuple(10)
type(out)

# %%

def return_tuple(variable):
    return variable, variable+2, variable+4

var, *junk = return_tuple(2)

print(type(var), var)
print(type(junk), junk)

# %%
# A common way to ignore the unncessary output from a function is to use underscore

var, *_ = return_tuple(2)

# %% md
# **Question**:
# What will be the length of ``_`` above?
#

# %%
# Above we were interested in only `var` and wanted to ignore everything else
# returned by `return_tuple` function.

# %%
# calling a function from another function
# ----------------------------------------

def foo(a):
    return a + 1

def bar(a):
    return foo(a) + 1

bar(1)

# %%
# Above we are calling function `foo` from inside function `bar`. The output of `foo` is
# added with 1 and returned by `bar`.

# %%

def foo(a):
    return a + 1

def bar(a):
    return a+100

def baz(a):
    b = foo(a)
    b = bar(b)
    return b

baz(1)

# %%
# Above we are calling function `foo` from inside function `baz`. The output of `foo` is
# assigned to variable `b` and then `bar` is called with `b` as input argument.
# The output of `bar` is again assigned to `b` and returned by `baz`.

# %%
# **Question**:
#
# .. code-block:: python
#
#    def add_nums(a, b):
#        return a + b
#
#    def sub_nums(a, b):
#        return a - b
#
#    def multiply_nums(a, b):
#        return a * b
#
#    def divide_nums(a, b):
#        return a / b
#
# Write a function named `foo` in such a way that you call all the 
# above four functions (`add_nums`, `sub_nums`, `multiply_nums`, `divide_nums`) 
# from inside `foo`. The `foo` function should take
# two input arguments and return 100. You can create intermediate variables as well.

# %% md
# function as input argument
# ---------------------------
# The input arguments to a function can be any python object. This includes
# functions as well. 
# We can assign a function to a variable and use that variable to call the function.

# %%

def print_me(to_print):
    print(to_print)

x = print_me

x('This goes into print_me')

# %% md
# Thus we can use functions as input arguments to other functions as well.

# %%

def magic(left, op, right):
    return op(left, right)

def my_op(var_a, var_b):
    return var_a == var_b

magic(2, my_op, 2)


# %% 
# positioning of ``return`` statement
# -----------------------------------
#
# It is important to understand that the function will exit as soon as it encounters
# a ``return`` statement. This means that the code after the ``return`` statement
# will not be executed.

# %%
def add_nums(a, b):
    return a + b
    print('This will not be printed')

add_nums(1, 2)

# %%

def add_nums(a_list, break_point=5):
    _sum = 0.0
    for val in a_list:
        _sum += val
        if _sum > break_point:
            break
    return _sum


x = add_nums([1, 2, 3, 4, 5])
print(x)

# %% md
# As soon as the value of `_sum` became greater than `break_point`, the ``for`` loop
# exited and we got the value of `_sum` at that point.

# %%

x = add_nums([1, 2, 3, 4, 5], 50)
print(x)

# %% md
# **Question:** 
# Was the ``break`` statement executed above?

# %%
# **Question**:
# What will be the output of following code?
#
# .. code-block:: python
#
#    def foo(a,b):
#        c = a+b
#        return c
#        c = a-b
#    z = foo(1,2)
#    print(z)

# %%
# **Question**:
# What will be the output of following code?
#
# .. code-block:: python
#
#    def foo(a,b):
#        c = a+b
#        return c
#        c = a-b
#        return c 
#    z = foo(1,2)
#    print(z)

# %% md
# **Question**:
# What will be the output of following code?
#
# .. code-block:: python
# 
#    def foo(a,b):
#        if a==0:
#            return b
#        else:
#            return foo(a-1, a+b)

# %% md
# docstring
# ----------
# The first string inside the functions is usually put for help. This is
# called `docstring`. It can be called by ``__doc__`` method

# %%

def fahrenheit(T_in_celsius):
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
