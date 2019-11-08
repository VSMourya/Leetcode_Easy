

def reverseInteger(x):
    out = int(str(abs(x))[::-1]) if x > 0 else int(str(abs(x))[::-1]) * -1
    if out > -2 ** 31 and out < 2 ** 31 - 1:
        return out
    else:
        return 0

x = int(input("Enter an Intput: "))

print(reverseInteger(x))