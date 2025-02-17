"""
__lt__
__gt__
__le__
__ge__
__eq__
__ne__
__hash__
__get__
__set__
__mul__
__sub__
__add__
__len__
"""


class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def __str__(self):
        return f"Name is : {self.name}"

    def __mul__(self, p):
        return f"{self.name}*{p.name}"

    def __sub__(self, p):
        return f"{self.name}-{p.name}"

    def __call__(self):
        return self.name

    def __len__(self):
        return len(self.name)


person = Person("Parry")
print(person)
p2 = Person("Parvez")
print(person*p2)
print(person-p2)
print(person())
print(len(person))
