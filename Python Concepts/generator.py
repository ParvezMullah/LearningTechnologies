"""
Return the lazy iterator. has yield
"""


def even_generator():
    x = 0
    while True:
        x += 2
        yield x


gen = even_generator()
print(next(gen))
print(next(gen))
print(next(gen))

for even in even_generator():
    print(even, end=" ")
    if even == 200:
        break
print()


def odd_generator():
    x = -1
    while x < 20:
        x += 2
        yield x


for odd in odd_generator():
    if odd > 20:
        break
    print(odd, end=" ")
