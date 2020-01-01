
def isHappy(n):

    hsh = {}

    while n not in hsh:
        hsh[n] = True
        ls = [int(i) for i in str(n)]
        n = sum([x ** 2 for x in ls])
        if n == 1:
            return True

    return False


num = 19
print(isHappy(num))