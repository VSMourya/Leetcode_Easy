


num = 10

for i in range(0,num):
    if i == 0 or i == num-1:
        print(" "*(num-i-1),end="*")
        print("*"*(num-1))

    else:

        print(" "*(num-i-1),end="*")
        print(" "*(num-2),end="*")
        print(" ")

