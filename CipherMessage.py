import itertools
a = list(itertools.permutations([1,2,3], r=1))
b = list(itertools.permutations([1,2,3], r=2))
c = list(itertools.permutations([1,2,3], r=3))

a = a + b + c

resp = [sum(x) for x in a]

print(resp)
