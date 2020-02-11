def numberOfSteps(num):
    count = 0

    while num != 0:
        if num % 2 == 0:
            count += 1
            num = num // 2
        else:
            count += 1
            num -= 1

    return count

if __name__ == '__main__':
    print(numberOfSteps(7))