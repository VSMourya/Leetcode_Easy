


def removeElement( nums, val):
    while(True):
        if val in nums:
            nums.remove(val)
        else:

            break
    return nums



nums = [3,2,2,3,6,7,8,2,4,6,6,1,2]
val = 6

print(removeElement(nums,val))

