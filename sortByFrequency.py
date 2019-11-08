

arr = [3,3,3,3,2,2,2,2,2,2,1,1,5,5,6,6,6,7,7]
hsh = {}

ls = []

for i in arr:
    if i not in hsh:
        hsh[i] = 1
    else:
        hsh[i] += 1


for key,value in hsh.items():
    ls.append([key,value])

print(hsh)
ls.sort(key=lambda x:x[1])
ls = ls[::-1]


final = ""
for i in range(len(ls)):
    item = ls[i]
    final += str(item[0])*item[1]

print(list(final))