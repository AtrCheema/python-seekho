"""
=============
2.8 pathlib
=============

.. important::
  This lesson is still under development.

"""
import os
from pathlib import Path

# %%
# Path
# -----

path = Path(os.getcwd())
print(path)

# %%
print(type(path))
