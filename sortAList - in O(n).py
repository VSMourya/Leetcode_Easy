
# sort the list which has contiguous elements having values within the range of length of list

def sortAList(ls):

    nums = [0]+ls
    n = len(nums)
    for i in range(len(ls)):
        nums[ls[i]%n] = ls[i]

    print(nums[1:])


ls = [3, 1, 4, 2]

print(sortAList(ls))