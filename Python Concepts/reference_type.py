def append_to_list(a=[]):
    a.append(10)
    return a

a = []

print(append_to_list(a)) # [10]
print(append_to_list()) # [10]
print(append_to_list()) #[10,10]
print(append_to_list()) #[10,10,10]

print("#"*40)

def append_to_list(b=[]):
    if b is None:
        b = []
    b.append(10)
    return a

b = []

print(append_to_list(b)) # [10]
print(append_to_list()) # [10]
print(append_to_list()) #[10]
print(append_to_list()) #[10]