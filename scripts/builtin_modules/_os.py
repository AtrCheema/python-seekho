"""
========
2.1 os
========

.. important::
  This lesson is still under development.

When python is installed, several modules/packages are pre-installed in it. These modules provide
some very basic functionality to the user. The ``os`` is such a built-in module which provides
the functionalities about paths or operating system.
"""

import os


# %%
# system()
# ========
# It is used to execute commands that we would otherwise execute using
# command prompt on windows or on terminal. For example on Windows we can
# do ``os.system(dir)`` where ``dir`` is a command for Windows command prompt
#
# .. code-block:: python
#
#    os.system(dir)
#

# %%
# getcwd()
# ========
# It returns the current working directory.
print(os.getcwd())

# %%
print(type(os.getcwd()))

# %%
# path
# =====
# The ``path`` submodule of ``os`` module contains several helpful functions
# to manipulate path.
#
# Find out whether the path `p` exists or not
p = os.getcwd()
os.path.isdir(p)

# %%
# Find out whther `p` is a file or not
os.path.isfile(p)

# %%
# ---

# Find the parent directory of `p`.
os.path.dirname(p)

# %%
# ---

os.path.abspath(p)

# %%
# ----

os.path.split(p)

# %%
# ---
os.path.basename(p)

# %%
# ---

os.path.exists(p)

# %%
# remove()
# ---------
# delete a file from disk

# %%
# replace()
# =========


# %%
# listdir
# =======
# Returns a list of folders/directories in a given path.
os.listdir(p)

# %%
# environ
# =======
environ = os.environ
print(environ)
print(type(environ))
print(len(environ))

# %%
# wait()
# =======

# %%
# rename()
# =========

# %%
# renames()
# =========

# %%
# mkdir()
# ========
# creates a directory if all its upper/parent directories are present.
new_folder = os.path.join(os.getcwd(), "NewFolder")

print(os.path.exists(new_folder))
os.mkdir(new_folder)

print(os.path.exists(new_folder))

# %%
p = os.path.join(os.getcwd(), "NonExistentFolder", "InsideNonExistentFolder")

print(os.path.exists(p))

# %%
# uncomment following line

# os.mkdir(p)  # FileNotFoundError

# %%
# os.makedirs
# ===========
os.makedirs(p)
print(os.path.exists(p))

# %%
# rmdir()
# =========

print(os.path.exists(new_folder))
os.rmdir(new_folder)
print(os.path.exists(new_folder))

# %%
# cpu_count()
# ===========
# Cound the number of cpus/cores/processes available.

print(os.cpu_count())

# %%
# chdir()
# ========
original_wd = os.getcwd()
print("Current working directory is \n", original_wd)
print(f"It has {len(os.listdir(os.getcwd()))} sub-directories/folders in it.")
new_wd = os.path.join(os.path.dirname(original_wd))
os.chdir(new_wd)
print("Now we have changed working directory to \n", new_wd)
print(f"This new directory has {len(os.listdir(os.getcwd()))} sub-directories/folders in it")
# now changing back to original
os.chdir(original_wd)

# %%
# walk
# ====
for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    print(dirpath, dirnames, filenames)

# %%
python_seekho_scripts = os.path.join(os.path.dirname((os.path.abspath(''))))
for dirpath, dirnames, filenames in os.walk(python_seekho_scripts):
    print(dirpath, dirnames, filenames)

# %%
# finding files
# =============
# Let's create few files first.

for i in range(5):
    with open(f'TextFile_{i}.txt', 'w'):
        pass
for i in range(5):
    with open(f'CsvFile_{i}.csv', 'w'):
        pass

# %%
# If we want to find all files and folders within a specific path

path_to_look = os.getcwd()

print(os.listdir(path_to_look))

# %%
# If we want to find only files and not folders/directories, we can do following
# list comprehension.

print([f for f in os.listdir(path_to_look) if os.path.isfile(f)])

# %%
# If we want to find files with a specific extension, we can do as following

print([f for f in os.listdir(path_to_look) if os.path.isfile(f) and f.endswith(".txt")])

# %%
# If we want to find files with a specific extension, and starting with a
# specific name, we can do as following
print([f for f in os.listdir(path_to_look) if os.path.isfile(f) and f.endswith(".txt") and f.startswith('TextFile_')])

# %%
# number of lessons in python-seekho book
scripts = [fname  for f in os.walk(python_seekho_scripts) for fname in f[2] if fname.endswith('.py')]
print(scripts)

# %%
print(f"Total number of lessons in python-seekho book are {len(scripts)}.")


