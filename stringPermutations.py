from itertools import permutations


a = input()
b =[]
l = permutations(a)

for j in list(l):
    b.append("".join(j))

print(*b)

