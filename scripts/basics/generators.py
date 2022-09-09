"""
=================
1.19 generators
=================
This lesson explains the concept of generators in python and the use of keyword
``yield``.
"""

# %%
# We know that we can do list comprehension as below,

print([i for i in range(10)])

# %%
# Similarly we can also do tuple comprehension

print((i for i in range(10)))

# %%
# However, we see that a tuple comprehension returns a generator.

# %%
a = (i**i for i in range(10))

# We can unpack generators using ``*`` as following
print(*a)

# %%
# iterating over generator
# ==========================
# We can use generators in a for loop because we can iterate over them.

a = (i for i in range(10))

for i in a:
    print(i)


# %%
# The ``next`` function on a generator is akin to running the for loop
# for one iteration. It means we want to get the next value from generator.

a = (i**i for i in range(10))
next(a)

# %%

next(a)

# %%

next(a)

# %%
# We can call the ``next`` function as long as the function is not exhausted.

# %%
# Running a for loop on a generator actually calls ``next`` function on the
# generator until it is exhausted.

for _ in a:
    pass

# %%
# Since all the iterations are complete, our generator is now exhausted.
# If we try to get next value from generator, it will throw an error.

# uncomment the following line
# next(reader)

# %%
# Here, when we created generator using tuple comprehension, we were just returning
# ``i`` but we can do a complicated or computationally heavy stuff e.g. reading a
# file at each iteration.


def read_file(idx):
    print(f"reading file {idx}")
    return idx


reader = (read_file(i) for i in range(10))

for _ in reader:
    pass

# %%
# or a memory intensive computation at each step.

a = (i**i for i in range(10))

for i in a:
    print(i)

# %%
# Working of generator
# ======================
# A generator actually breaks the computation flow in a for loop
# and executes the commands inside the for loop one by one. This helps
# in executing the memory intensive work one by one instead of executing
# all the code at once. For example, instead of reading all the 10 files
# at once and then processing them, we read one file at one time, process
# it and then read the next file.
#

# %%
# yield
# --------
# How to generate a generator using ``yield`` keyword?


def read_files(num_files):
    file_content = []
    for f in range(num_files):
        _file_content = read_file(f)
        file_content.append(_file_content)
    return


read_files(10)

# %%
# Above we are reading all the files and saving their content in a list at once.
# If the files are large and we don't need all the files at once,
# then we would like to read one file, use/process its contents and then read the next file.
# In such a case, we would like to write a function, which reads one file at
# a time. This can be accomplished by using ``yield`` keyword.

# %%


def read_files(num_files):
    for f in range(num_files):
        yield read_file(f)


reader = read_files(10)

print(type(reader))

# %%
# Let's iterate through the generator

for _ in reader:
    pass

# %%
# We can not have any statement in a function after ``return`` keyword. However,
# we can have statements after ``yield``. These statements are executed at the next iteration.


def read_files(num_files):
    print("entering read_files function")
    for f in range(num_files):
        print(f"at iteration {f}")
        yield read_file(f)
        print(f"at iteration {f} after yield")


reader = read_files(10)

next(reader)

# %%
# We see that the string **at iteration {f} after yield** is not printed yet.
# This is because only first iteration of for loop is complete. However,
# this string will be printed at the start of next iteration.

next(reader)


# %%
# When a function has ``yield`` keyword, we can have statements even
# outside the for loop. All the statements outside the for loop will
# be executed after the last iteration of the generator.

def read_files(num_files):
    print("entering read_files function")
    for f in range(num_files):
        print(f"at iteration {f}")
        yield read_file(f)
        print(f"at iteration {f} after yield")
    print('end of for loop')
    return


reader = read_files(10)

print(type(reader))

# %%

for _ in reader:
    pass

# %%
# We wee that the string `end of for loo` is printed only once at the end.

# %%
# yield from
# ----------
# Consider the case where we have a list which further consists of one or more lists

my_list = [1, 2, [3, 4], 5]

# %%
# If we want to yield one element from
# this list by flattening it, the naive approach would be following


def flatten(elements):
    for elem in elements:
        if isinstance(elem, list):
            for _elem in elem:
                yield _elem
        else:
            yield elem


flattener = flatten(my_list)

for i in flattener:
    print(i)

# %%
# Above we iterate over each value (elem) of my_list. Whenever, ``elem`` is itself a list,
# we make another ``for`` loop.
#
# However, we can achieve the same thing using ``yield from`` keyword.


def flatten(elements):
    for elem in elements:
        if isinstance(elem, list):
            yield from elem
        else:
            yield elem


# %%
# Above, instead of writing another ``for`` loop for ``elem``, we are using the keyword
# ``yield from``.

flattener = flatten([1, 2, [3, 4], 5])

for i in flattener:
    print(i)

# %%
# What if we have list inside list of another list or a variation of such nested
# lists?

# %%
flattener = flatten([1, 2, [3, 4], 5, [6, [7, 8]]])

for i in flattener:
    print(i)

# %%
# ``[7,8]`` is printed in same line, which means this inner list is not flattened
# by our function.

# %%
# We may be tempted to add another ``if`` statement for checking whether any member
# in ``elem`` is a list or not. However, we can call the ``flatten`` function from
# inside so that the recursion continues until we flatten the list
# to its last/innermost member.


def flatten(elements):
    for elem in elements:
        if isinstance(elem, list):
            yield from flatten(elem)  # we call the function again
        else:
            yield elem


flattener = flatten([1, 2, [3, 4], 5, [6, [7, 8]]])

for i in flattener:
    print(i)
# %%
# Now the list is flattened to its innermost member.

# %%
flattener = flatten([1, 2, [3, 4], 5, [6, [7, [8, 9, 10]]]])

for i in flattener:
    print(i)
