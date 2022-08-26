"""
1. An Iterator is an object.
2. It remembers its state.
3. __iter__ method initializer an iterator.
4. __next__ returns the next element. upon reaching end of an iteration it must return StopIteration.

Iterator                        Vs                          Generator
class based                                             function based
does not store local variable                           does store local variable.
It returns                                              It yield
every iterator is not generator                         Every generator is iterator.


"""

class ArrayList:
    def __init__(self, arr) -> None:
        self.arr = arr

    def __iter__(self):
        self.pos = -1
        return self

    def __next__(self):
        if self.pos < len(self.arr) - 1:
            self.pos += 1
            return self.arr[self.pos]
        raise StopIteration("No More Items To Get.")


arr = ArrayList([1,2,3,4])
iterator = iter(arr)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator))

        