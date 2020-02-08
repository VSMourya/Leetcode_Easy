import math
def judgeSquareSum(c):
    hsh = set()

    count = int(math.sqrt(c))
    for i in range(count + 1):
        hsh.add(i ** 2)

    for i in hsh:
        if c - i in hsh:
            return True

    return False

if __name__ == '__main__':
    print(judgeSquareSum(5))

    # Input: 5
    # Output: True
    # Explanation: 1 * 1 + 2 * 2 = 5