


N = int(input("Enter = "))

ls= []

a = "fizz"
b = "bizz"
ab = "fizzbizz"

for i in range(1,N+1):

    if i%3 == 0 and i%5 ==0:
        ls.append(ab)
        continue

    else:
        if i%3 == 0:
            ls.append(a)
            continue

        if i%5 == 0:
            ls.append(b)
            continue

    ls.append(str(i))

print(ls)































