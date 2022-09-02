"""
======================
15. getattr vs setattr
======================
This lesson shows the usage of ``setattr`` and ``getattr``
"""

class Human:

    def __init__(self, name):
        self.name = name

    def grow(self):
        setattr(self, 'empathy', 10)
        return

human = Human("Ali")

# uncomment following line
# human.empathy

#%%

human.grow()

human.empathy

#%%

setattr(human, "empathy", 14)

human.empathy

#%%

class Human:

    def __init__(self, name):
        self.name = name

    def grow(self):
        setattr(self, 'empathy', 10)
        return

    def info(self):
        empathy = getattr(self, 'empathy', None)
        return empathy

human = Human("Ali")

#%%
# uncomment following line
# human.empathy

#%%

human.info()

#%%

human.grow()
human.info()
