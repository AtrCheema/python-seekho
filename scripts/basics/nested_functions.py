"""
=======================
1.15 nested functions
=======================
"""

# %% md
# A nested function is a function inside a function.


# %%

def percent(x, n):
    def number():
        factor = n / 100
        print(x * factor)

    number()


percent(120, 10)

# %% md
# It is pertinent to note that the function ``number`` was able to use the variable ``x``
# and ``n`` which are from outer function ``percent``.

# %%
# In following example, the inner function is making use of variable ``factor`` which
# is defined inside the outer function ``percent``.

def percent(x, n):
    factor = n / 100

    def number(xx):
        print(xx * factor)

    number(x)


percent(120, 10)

# %% md
# It is more clear now that inner function can make use of variables from outer functions.

#%%
# In following example, the outer function returns the inner function which can be used later on.


# %%

def percent(n):
    factor = n / 100

    def number(xx):
        print(xx * factor)

    return number


ten_percent = percent(10)  # execution of percent is finished
ten_percent(150)  # variable `factor` is still remembered/used

#%%
# When we called the ``percent`` function, it returned the inner function ``number``.
# We assigned this inner function to a variable ``ten_percent``. Now we can use this
# variable to call the inner function. The inner function still remembers the value of
# ``factor`` which was set when we called the outer function ``percent``. Thus when 
# we call ``ten_percent(150)``, it is actually calling the inner function ``number`` with
# the value of ``factor`` set to 0.1.

two_percent = percent(2)
two_percent(150)

# %%

ten_percent(300)  # factor is 0.1

# %% md
# The variable ``factor`` is linked
# with the inner function and so with ``ten_percent`` and ``two_percent``. Both ``ten_percent``
# and ``two_percent`` have different values of ``factor`` associated with them. It is worth
# noting that, even when the execution of function ``percent`` is finished, its
# variable ``factor`` is still remembered by ``ten_percent`` and ``two_percent``.We can
# find out which value of ``factor`` is associated with ``ten_percent`` and which value
# is associated with ``two_percent``.

# %%

ten_percent.__closure__[0].cell_contents

# %%

two_percent.__closure__[0].cell_contents

# %% md
# Although we finished execution of function ``percent`` in previous cell, but upon executing
# ``ten_percent(300)``, the function ``number``, still remembers that what ``factor`` it has to
# multiply with.  In this way we link a certain data with a function.

# %%
# **Question**: Following the same method as above, define a function which returns 33% of a number.
# Then use this function to find 33% of 300.

def full_name(first_n):
    prefix = 'Mr. '

    def family_name(fam_name):
        suffix = 'sahab'

        def kuniyat(z):
            return prefix + first_n + ' ' + fam_name + ' ' + z + ' ' + suffix

        return kuniyat

    return family_name


# %%

full_name('Abdus')('Sattar')('Edhi')

# %%

fam_name = full_name('Rashid')  # fam_name is intermediate function

# %%

Kuniyat = fam_name('Minhas')  # kuniyat is innermost function

# %%

Kuniyat('Shaheed')  # Kuniyat is innermost function

# %% md
# Why use nested function
#
# * They can be used to avoid global variables. In upper example, the variable ``prefix``,
#   can be set as global variable outside ``full_name``, but in this case we have made data
#   encapsulation and now the variable `prefix` is only available inside the function
#   where it is actually needed. This is also called information hiding.
#
# * To improve readability. If there is a tiny function that will only be invoked by the
# outer function, then this will help us determine what the function is all about.


# %%

def print_name(name, gender):
    def add_prefix(s):
        if s == 'Male':
            return 'Mr.'
        else:
            return 'Mrs.'

    print(add_prefix(gender), name)


print_name('lalak jan', 'Male')

print_name('Fatima Jinnah', 'female')

# %% md
# We could have easily put ``add_prefix`` outside the function in outer scope, but in current case
# when we will read the code, it becomes clear to us that the function ``add_prefix`` is used
# only inside ``print_name``

# %%

def add_family_name(fam_name):
    def make_name(first):
        return first + fam_name

    return make_name


name_maker = add_family_name(' Minhas')
name_maker('Rashid')


# %% md
# ``nonlocal`` statement
#-----------------------

# %%

def square_after_adding_one(_in):
    x = _in

    def add_one():
        x += 1  # trying to re-assign value of variable `x` from outer scope
        return x

    val = add_one() ** 2
    print(val)

#%%

# uncomment following line
# square_after_adding_one(2)  # -> UnboundLocalError local variable 'x' referenced before assignment

# %%

x = 0


def square_after_adding_one(_in):
    x = _in

    def add_one():
        nonlocal x
        x += 1
        return x

    val = add_one() ** 2
    print(val, 'squared after adding 1')


print(x, 'global ')
square_after_adding_one(2)
print(x, 'global ')

# %%
# Above, the initial value of `x` is 0. Inside the function `square_after_adding_one`,
# we create a variable `x` with value 2. 
# At this point this `x` is different from the global `x`.
# Then we call `add_one` which increments `x` by 1. Note that here we are using `nonlocal` keyword.
# This keyword is used to tell the function that the variable `x` is not local to the function `add_one`
# Therefore, we are using the variable `x` from the outer function `square_after_adding_one` whose
# value is 2. So, `x` is incremented by 1 and then squared. The output is 9.
# Once we are outside the function `square_after_adding_one`, the global `x` is still 0 because
# we have not touched the global `x` inside the function `square_after_adding_one`.

x = 0


def square_after_adding_one(_in):
    x = _in

    def add_one():
        global x
        x += 1
        return x

    val = add_one() ** 2
    print(val, 'squared after adding 1')
    print(x, 'in outer function')


print(x, 'global ')
square_after_adding_one(2)
print(x, 'global ')

# %% md
# In above example, we are using `global` keyword instead of `nonlocal`. This means that we are
# using the global variable `x` inside the function `add_one`. Therefore, we are adding `1` to the
# global `x` whose value is `0`. So, `x` becomes `1` and then squared. Thus the value of ``val`` is `1`.
# There is another variable `x` which is inside the function `square_after_adding_one` whose value is `2`.
# This variable is not used inside the function `add_one`. 
