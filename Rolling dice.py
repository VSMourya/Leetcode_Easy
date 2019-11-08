





a = [1,2,3,4,5,6]
target = 6

ls = []


for i in range (len(a)):
    num = a[i]
    for j in range(0,len(a)):
        if a[j] + num == target:
            ls1 = []
            ls1.append(a[j])
            ls1.append(a[i])
            ls.append(ls1)
        else:
            continue

print(ls)


