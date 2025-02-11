#https://www.youtube.com/watch?v=AY62z7HrghY&list=PLIUOU7oqGTLhlWpTz4NnuT3FekouIVlqc&index=1

"""
Jaccard similarity
jaccard = intersection(A,B) / union(A/B)
"""
def jaccard(a: str, b: str) -> float:
    a_set = set(a.split())
    b_set = set(b.split())
    shared = a_set.intersection(b_set)
    union = a_set.union(b_set)
    return len(shared)/len(union)

print(jaccard("a b", "a c d"))

"""
w-shingling

works on ngram
"""
a = "his thought process was so many levels that he gave himself a phobia of heights"
b = "there is an art to getting your way and throwing bananas on to the street is not it"
c = "it is not often you find soggy bananas on the street"

a = a.split()
a_2gram = set([' '.join([a[pos], a[pos+1]]) for pos in range(len(a)-1)])

b = b.split()
b_2gram = set([' '.join([b[pos], b[pos+1]]) for pos in range(len(b)-1)])

c = c.split()
c_2gram = set([' '.join([c[pos], c[pos+1]]) for pos in range(len(c)-1)])


def jaccard_on_set(a: set, b: set) -> float:
    shared = a.intersection(b)
    union = a.union(b)
    return len(shared)/len(union)

print(jaccard_on_set(a_2gram,b_2gram))
print(jaccard_on_set(b_2gram,c_2gram))

"""
Lavenshtein
"""