def majorityElement(nums):
    hsh = {}

    for i in nums:
        if i not in hsh:
            hsh[i] = 1
        else:
            hsh[i] += 1

    num = -1
    mx = float("-inf")
    for key, value in hsh.items():
        if mx < value:
            mx = value
            num = key

    return num

if __name__ == '__main__':
    nums = [2,2,1,1,1,2,2]
    print(majorityElement(nums))