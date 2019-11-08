



def isRootPrime(number):

    root = int(number**0.5)

    for i in range(2, root // 2):
        if int(root % i) == 0:
            return "Root of the given number IS NOT A PRIME NUMBER"

    return "Root of the given number IS A PRIME NUMBER"

print(isRootPrime(289))
