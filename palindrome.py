

def palindrome(x):
    x1 = x
    num = 0
    if x < 0 :

        print("false")
    else:
        while (x1 > 0):
            rem = x1%10
            num = num*10 + rem
            x1 = x1//10

        if x == num:

            print("true")
        else:
            print("false")






x = int(input("Enter a number : "))
palindrome(x)