
def missingNumber(num):
    ls = 0
    count = 0

    for i in range(0, len(num) + 1):
        if i in num:
            continue
        else:
            count += 1
            ls = i
    if count != 1:
        return 1
    else:
        return ls


nums = [0,1]

print(missingNumber(nums))