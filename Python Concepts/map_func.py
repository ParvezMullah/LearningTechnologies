"""
map() function returns a map object(which is an iterator) 
of the results after applying the given function to each item 
of a given iterable (list, tuple etc.)
"""


def calculate_square(x):
    return x**2


input_list = [1, 2, 3, 4]
squared_list = list(map(calculate_square, input_list))
print(squared_list)
