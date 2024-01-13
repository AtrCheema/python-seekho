"""
============
2.10 random
============

.. important::
  This lesson is still under development.

"""

import random


# %%
# random
# --------------
# We can use random function to generate a random number between 0 and 1.
print(random.random())

# %%
# every time we call ``random.random()``, the result will be different and therefore unpredictable

print(random.random())

# %%
print(random.random())

# %%
# randint
# --------------
# If we want to generate a random integer between two ranges, we can make use of
# randint.

print(random.randint(1, 10))

# %%
# choice()
# --------------
# If we want to select a value randomly from a given sequence, we can make use of
# random.choice function.

random.choice([1,2,3,4])

# %%
random.choice([1,2,3,4])

# %%
# choices()
# --------------
# However, if we want to select more than one value, but randomly, from a sequence,
# we can then make use of random.choices.

random.choices([1,2,3,4,5, 6, 7])

# %%
random.choices([1,2,3,4,5], k=2)

# %%
# sample()
# --------------
# The sample function is very much similar to ``choices`` function.

random.sample([1,2,3,4,5], k=2)

dakoos = ['generals', 'siyasatdan', 'bureaucracy', 'saiths', 'anchors']
random.sample(dakoos, k=2)

# %%
# seed()
# --------------
# Suppose someone is making use of ``random.random()`` function in his script and getting
# some results. If you use the same script, your result will be different because
# we have seen that ``random()`` function generates a different number upon every
# call.
#
# How can we make use of random() function and still get reproducible results?
#
# The seed function from random module is used to generate reproducible results.
# Let's generate five random numbers using random.random() function inside a for loop.

for i in range(5):
  print(random.random())

# %%
# The above five numbers are `completely` random in the sense that we can not
# predict, what would be the next number. If we call the random.random() again,
# the newly generated random numbers will again be random and unpredictable.

for i in range(5):
  print(random.random())

# %%
# Now, Let's set the random seed and then generate the random numbers using random.random()

random.seed(313)

for i in range(5):
  print(random.random())

# %%
# We have generated 5 random numbers so far after setting the ranomd seed with 313.
# If we reset the random seed again, the next five random numbers that will be
# generated will be exactly same as the first five random numbers that were generated (above)
# when we had set the seed to 313 initially.

random.seed(313)

for i in range(5):
  print(random.random())

# %%
# This means, every time we set the random seed, the generated numbers will be
# random but reproducible.

# %%
# **Question**:
# (Can you) Predict the random numbers generated as a result of following code?

# random.seed(92)
# for i in range(5):
#   print(random.random())

# %%
# Consider for example a function which uses random numbers in it using ``random.random()``.
# Now every time we run the function, the results will be different. This means the output
# of our function will not be reproducible. We can set the random seed either globally (at the start of script)
# or locally (inside the function) in order to make our results reproducible.

# %%
# **Question**:
# What will be the last value printed by the following code?

# random.seed(313)
# for i in range(7):
#   print(random.random())

# %%
# Setting the random seed does not only affect random.random() function,
# but if affects all functions of random module. Consider for example
# random.choice function.

for _ in range(3):
  print(random.choice(dakoos))

# %%
random.seed(313)

for _ in range(3):
  print(random.choice(dakoos))

# %%
random.seed(313)

for _ in range(3):
  print(random.choice(dakoos))

# %%
# shuffle()
# --------------
print(dakoos)

random.shuffle(dakoos)

print(dakoos)

# %%
random.shuffle(dakoos)

print(dakoos)

# %%
# **Question**:
# Write a function called ``pseudo_shuffle``, which suffles the `dakoos` list, but
# the order of values in the returned/shuffled list is always same. This means
# calling ``pseudo_shuffle(dakoos)`` multile times return same order in the list.
# It should be noted that the function ``pseudo_shuffle`` must make use of ``random.suffle`` function
# inside it.

# %%
# randrange
# --------------

random.randrange(1, 10)

# %%

random.randrange(1, 10, step=2)

# %%
# getstate()
# --------------

# %%
# setstate()
#--------------

# %%
# distributions
#--------------