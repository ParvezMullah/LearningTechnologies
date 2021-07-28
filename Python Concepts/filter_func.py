"""
The filter() method filters the given sequence with the help of a function 
that tests each element in the sequence to be true or not.
"""


def is_even(num):
    return num % 2 == 0


x = [1, 2, 3, 4, 5, 6, 7, 8, 9]

filter_x = list(filter(is_even, x))
print(filter_x)
