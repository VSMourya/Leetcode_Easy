def findLengthOfLCIS(nums):
    if not nums:
        return 0

    stack = [nums[0]]
    lens = 0

    for i in range(1, len(nums)):
        if nums[i] > stack[-1]:
            stack.append(nums[i])
        else:
            if len(stack) > lens:
                lens = len(stack)
            stack.clear()
            stack.append(nums[i])

    return len(stack) if len(stack) > lens else lens

if __name__ == '__main__':
    nums = [1,3,5,4,7]
    print(findLengthOfLCIS(nums))