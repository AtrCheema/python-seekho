"""
=========================
2.3 time and dateandtime
=========================

.. important::
  This lesson is still under development.

"""

# %% md
# time
# ======

import time

# %%
# time()

time.time()

# %%

start = time.time()

# do something

print(time.time() - start, "seconds")


# %%
# sleep()

for i in range(5):
    time.sleep(0.5)
    print(i, end = " ")

# %%
# asctime()
from time import asctime
asctime()

# %%
# clock()


# %%
# daylight


# %%
# localtime()

print(time.localtime())

# %%
# timezone


# %%
# ctime()

print(time.ctime())

# %% md
# datetime
# =========

from datetime import datetime

# %%
# datetime.now()

now = datetime.now()

print(now)

# %%

print(type(now))

# %%
# datetime.ctime()
datetime.ctime(now)

# %%
# datetime.strftime()

print(datetime.strftime(now, "%Y-%m-%d %H:%M:%S"))

# %%
# datetime.strptime()

# %%
# datetime.isoformat()

datetime.isoformat(now)

# %%

datetime.isoformat(now, sep=" ")

# %%
# datetime.fromisoformat()

# %%
# datetime.toordinal()

# %%
# datetime.fromtimestamp()

# %%
# timedelta
# ---------

from datetime import timedelta

current = datetime.now()

current + timedelta(seconds=10)

# %%

current + timedelta(days=10)

# %%

current + timedelta(weeks=10)

# %%

current - timedelta(hours=10)

# %%
# We can compare two datetime objects

past = current - timedelta(hours=10)

current > past

# %%

current < past

# %%

future = current + timedelta(hours=10)

current < future

# %%

current > future

# %%
# strftime()

now.strftime("%Y%m%d_%H%M%S")

# %%

now.strftime("%d %B %Y %H:%M:%S")