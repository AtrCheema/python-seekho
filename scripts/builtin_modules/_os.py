"""
========
2.1 os
========
"""

import os


# %%
# system()


# %%
# path


# %%
# remove()


# %%
# rmdir()


# %%
# replace()


# %%
# getcwd()


# %%
# open()


# %%
# write()


# %%
# close()



# %%
# listdir


# %%
# environ


# %%
# wait()


# %%
# rename()


# %%
# renames()


# %%
# mkdir()


# %%
# cpu_count()

# %%
# chdir()


#%%
# finding files
#---------------
# Let's create few files first.

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


