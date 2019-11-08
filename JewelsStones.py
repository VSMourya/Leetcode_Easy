



J = "abA"
S = "AAbbbaa"

hsh = {}
count =0



for x in S:
    if x not in hsh:
        hsh[x] =1
    else:
        hsh[x] +=1

for i in J :
    if i in S :
        count = count + hsh[i]
    else:
        continue

print(count)


