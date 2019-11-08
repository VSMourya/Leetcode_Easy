

#noOfStairs that can be formed with n boxes


n = int(input("enter : "))
n1  = n
steps = 0

count = 1

while count < n :
    if count-1 < n1 :
        steps +=1
        n1 = n1-count
        count +=1
    else:
        break

print(steps)








