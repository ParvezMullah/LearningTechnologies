"""
It accepts callable and returns a callable.
"""

def decorator2(func):
    def inner_func(*args, **kwargs):
        print("decorator2")
        return func()
    return inner_func


def decorator1(func):
    def inner_func(*args, **kwargs):
        print("decorator1")
        print("args", args)
        print("kargs", kwargs)
        return func(args, kwargs)

    return inner_func

@decorator2
@decorator1
def decorated_func(name, age):
    print("I am decorated.")


decorated_func(name="parvez", age="25")
