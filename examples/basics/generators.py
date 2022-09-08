"""
=================
1.19 generators
=================
This lesson explains the concept of generators in python and the use of keyword
``yield``.
"""

#%%
# We know that we can do list comprehension as below
print([i for i in range(10)])

#%%
# Similarly we can also do tuple comprehension similarly

a = (i for i in range(10))

print(type(a))

#%%
# However, we see that a tuple comprehension returns a generator.
#
# We can use generators in a for loop because we can iterate over them

for i in a:
    print(i)

#%%
# Here, when we create generator using tuple comprehension, we were just returning
# ``i`` but we can do a complicated or computationally heavy stuff e.g. reading a
# file at each iteration.

def read_file(idx):
    print(f"reading file number {idx}")
    return idx

a = (read_file(i) for i in range(10))

for _ in a:
    pass

#%%
# or a memory intensive computation at each step

a = (i**i for i in range(10))

for i in a:
    print(i)

#%%
# A generator actually breaks the computation flow in a for loop
# and executes the commands inside the for loop one by one. This helps
# in executing the memory intensive work one by one instead of executing
# all the code at once. For example, instead of reading all the 10 files
# at once and then processing them, we read one file at one time, process
# it and then read the next file.
#

a = (i**i for i in range(10))

#%%
# since ``a`` is a generator, we can unpack it as following
print(*a)

#%%

def read_files(num_files):
    file_content = []
    for f in range(num_files):
        _file_content = read_file(f)
        file_content.append(_file_content)
    return

read_files(10)

#%%
# Above we are reading all the files and saving their conent in a list at once.
# If the files are large and we don't need all the files at once,
# then we would like to read one file, use/process its contents and then read the next file.
# In such a case, we would like to write a function, which reads one file at
# a time. This can be accomplied by using ``yield`` statement

#%%

def read_files(num_files):
    for f in range(num_files):
        yield read_file(f)

reader = read_files(10)

print(type(reader))

#%%
# Let's iterate through the generator

for _ in reader:
    pass

#%%
# We can not have any statement in a function after ``return`` statement. However,
# we can have statements after ``yield``. These statements are executed at the next iteration

def read_files(num_files):
    print("entering read_files function")
    for f in range(num_files):
        print(f"at iteration {f}")
        yield read_file(f)
        print(f"at iteration {f} after yield")


reader = read_files(10)

next(reader)

#%%
# We see that the string **at iteration {f} after yield** is not printed yet.
# This is because only first iteration of for loop is complete. However,
# this string will be printed at the start of next iteration now.

for _ in reader:
    pass

#%%
# Since all the iterations are complete, our generator is now exausted.
# If we try to get next value from generator, it will throw an error.

# uncomment the following line
# next(reader)

#%%
# The ``next`` function on a generator is akin to running the for loop
# for one iteration. It means we want to get the next value from generator.

reader = read_files(10)

print(next(reader))

#%%

print(next(reader))

#%%

print(next(reader))

#%%
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
#%%

for _ in reader:
    pass

#%%
# Consider the case where we have following list

mylist = [1,2,[3,4], 5]

#%%
# This list further consists of list. If we want to yield one element from
# this list by flattening it, the naive approach would be following

def flatten(elements):
    for elem in elements:
        if isinstance(elem, list):
            for _elem in elem:
                yield _elem
        else:
            yield elem

flattener = flatten(mylist)

for i in flattener:
    print(i)

#%%
# Above we iterate over each elem of mylist. Whenever, ``elem`` is itself a list,
# we make another ``for`` loop.
#
# However, we can acheive same using ``yeild from`` keyword.

def flatten(elements):
    for elem in elements:
        if isinstance(elem, list):
            yield from elem
        else:
            yield elem

#%%
# Above, instead of writing another ``for`` loop for ``elem``, we are using the keyword
# ``yield from``.

flattener = flatten([1,2,[3,4], 5])

for i in flattener:
    print(i)

#%%
# but what if we have list inside list of another list or a variation of such nested
# lists

# %%
flattener = flatten([1, 2, [3, 4], 5, [6, [7, 8]]])

for i in flattener:
    print(i)

#%%
# ``[7,8]`` is printed in same line, which means this inner list is not flattened
# by our function.

#%%
# Instead of adding another ``if`` statement for checking whetehr any member
# in ``elem`` is a list or not, we can call the ``flatten`` function from
# inside so that the recursion continues untill we flatten the list
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
#%%
# Now the list is flattened to its innermost member

#%%
flattener = flatten([1, 2, [3, 4], 5, [6, [7, [8, 9, 10]]]])

for i in flattener:
    print(i)