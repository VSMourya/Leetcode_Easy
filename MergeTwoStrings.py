#MergeTwoStrings




a,b = map(str,input("Enter 2 strings such that len(1st string) > len(2ns string) = ").split(" "))


a = list(a)
b = list(b)

str = ""
count = 0

lenMax = max(len(a),len(b))
lenMin = min(len(a),len(b))

for i in range(0,lenMax):
    str = str + a[i]
    for j in range(count,lenMin):
        str = str + b[j]
        count+= 1
        break

print(str)


