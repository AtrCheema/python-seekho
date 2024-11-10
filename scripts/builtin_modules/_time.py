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

start = time.time()

# do something

print(time.time() - start, "seconds")


# %%
# sleep()

for i in range(5):
    time.sleep(0.5)
    print(i, end = " ")


# %%
# strftime()


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


# %%
# timezone


# %%
# ctime()



# %% md
# datetime
# =========

from datetime import datetime


# %%
# datetime.ctime()


# %%
# datetime.now()

now = datetime.now()

print(now)

# %%

print(type(now))

# %%
# datetime.strftime()

print(datetime.strftime(now, "%Y-%m-%d %H:%M:%S"))

# %%
# datetime.strptime()

# %%
# datetime.isoformat()

# %%
# datetime.fromisoformat()

# %%
# datetime.toordinal()

# %%
# datetime.fromtimestamp()

# %%
# timedelta

from datetime import timedelta

current_time = datetime.now()

current_time + timedelta(seconds=10)

# %%

current_time + timedelta(days=10)

# %%

current_time + timedelta(weeks=10)

# %%

current_time - timedelta(hours=10)