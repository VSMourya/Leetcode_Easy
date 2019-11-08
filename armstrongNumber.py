
#Python Program to Check Armstrong Number

# A number is said to be an armstrong number
# if the number is equal to the sum of the squares of its individual numbers
# ex- 153 = 1*1*1 + 5*5*5 + 3*3*3  // 153 is an Armstrong number.


def isArmstrongNumber(number,length):

    output = 0
    counter = 0

    while counter < length:
        output = output + int(str(number)[counter])**length
        counter+=1

    print(output)

    if output == number:
        return True
    else:
        return False

number = int(input())
length = len(str(number))
print(isArmstrongNumber(number,length))

