"""
Anonymous function. Function without name
"""
is_even_lambda = lambda x :  x % 2 == 0


print("1 is even", is_even_lambda(1))
print("2 is even", is_even_lambda(2))


get_addition_lambda = lambda x, y: x + y
print(get_addition_lambda(1, 2))