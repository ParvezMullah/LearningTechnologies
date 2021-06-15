class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def fullname(self):
        return self.first + ' ' + self.last

    @fullname.setter
    def fullname(self, value):
        self.first, self.last = value.split(' ')

    @fullname.deleter
    def fullname(self):
        self.first, self.last = "", ""


emp = Employee("Parvez", "Mullah")
print(emp.fullname)
emp.fullname = "Parry Rocks"
print(emp.fullname)
del emp.fullname
print(emp.fullname)
