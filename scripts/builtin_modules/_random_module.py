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
# Generate a random number between 0 and 1.
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
#--------------
random.sample([1,2,3,4,5], k=2)

dakoos = ['generals', 'siyasatdan', 'bureaucracy', 'saiths', 'anchors']
random.sample(dakoos, k=2)

# %%
# seed()
# --------------
# The seed function from random module is used to generate reproducible results.
# Let's call generate five random numbers using random.random() inside the loop.

for i in range(5):
  print(random.random())

# %%
# The above five numbers are ""completely"" random in the sense that we can not
# predict that what would be the next number. If we call the random.random() again,
# the new generated random numbers will again be random.

for i in range(5):
  print(random.random())

# %%
# However, if se set the random seed and then generate the random numbers using random.random()
# the results will be reproducible.

random.seed(313)

for i in range(5):
  print(random.random())

# %%
# We have generated 5 random numbers so far after setting the ranomd seed with 313.
# If we reset the random seed again, the next five random numbers that will be
# generated will be exactly same as the first five random numbers that were generated
# when we had set the seed to 313 initially.

random.seed(313)

for i in range(5):
  print(random.random())

# %%
# This means, every time we set the random seed, the generated numbers will be
# random but reproducible.
#
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
random.shuffle(dakoos)

print(dakoos)

# %%
random.shuffle(dakoos)

print(dakoos)

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