"""
__new__:
    Primarily to allow programmers to subclass built in immutable types.
    also, we can create singelaton pattern.
    it calls __init__

__init__:
    Initialize object.

__call__:
    it is called when object of the class is called. makes object like a function.
"""

class A:
    def __init__(self):
        print("Init is called")

    def __new__(cls, *args, **kwargs):
        print(f"new is called. args : {args}, kwds : {kwargs}")
        return super().__new__(cls)

a = A()

class UpperClassTuple(tuple):

    def __new__(cls, iterable):
        __iterable = (item.upper() for item in iterable)
        return super().__new__(cls, __iterable)

    # def __init__(self, iterable):
    #     pass

upper_class_tuple = UpperClassTuple(("hi", "iam", "nobody"))
print(upper_class_tuple)


class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


gangadhar = Singleton()
shaktiman = Singleton()
print(f"gangadhar is shaktiman: {gangadhar is shaktiman}")



class Pay:
    def __init__(self, hourly_wages):
        self.hourly_wages = hourly_wages
        self.total_hour = 0
        self.total_pay = 0

    def __call__(self, hours_worked):
        self.total_hour += hours_worked
        self.total_pay += self.hourly_wages*hours_worked
        return self.total_hour, self.total_pay


pay = Pay(10)
print(f"Week 1 Total Hours Worked: {pay.total_hour}, Total Wages: {pay.total_pay}")
pay(10)
print(f"Week 2 Total Hours Worked: {pay.total_hour}, Total Wages: {pay.total_pay}")
pay(10)
print(f"Week 3 Total Hours Worked: {pay.total_hour}, Total Wages: {pay.total_pay}")
pay(20)
print(f"Week 3 Total Hours Worked: {pay.total_hour}, Total Wages: {pay.total_pay}")
