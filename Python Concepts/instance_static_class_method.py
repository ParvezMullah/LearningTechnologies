"""
instance method: takes instance as first argument
class method: takes class as first argument
static method
"""

class SomeClass:
    default_val = 1

    def __init__(self):
        pass

    def get_val(self):
        return self.default_val

    @classmethod
    def get_val_class(cls):
        return cls.default_val

    @staticmethod
    def get_val_static():
        return "I have no access"


obj1 = SomeClass()

obj2 = SomeClass()

obj1.default_val = 3
# SomeClass.default_val = 2

print(obj1.default_val)
print(obj1.get_val())
print(obj1.get_val_class())
print(obj1.get_val_static())
print(SomeClass.get_val_static())

print("*"*30)
print(obj2.default_val)
