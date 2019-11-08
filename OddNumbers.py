


def OddNumbers(a,b):

    oddNums = []
    for i in range(a,b):
        if i%2 !=0:
            oddNums.append(i)
        else:
            continue

    return oddNums

a = int(input("Number 1 = "))
b = int(input("Number 2 = "))


if 1<=a<=10**19 and a<b:
   if 1<=b<=10**19:
        print(*OddNumbers(a, b))
else:
    print("sorry")








