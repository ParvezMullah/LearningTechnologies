"""
str : display
repr: unambiguous
"""

from datetime import datetime
names = ["parvez", "parry", "atif"]
print(names)
print(str(names))
print(repr(names))


now = datetime.now()
print(now)
print(str(now))
print(repr(now))
