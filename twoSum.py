
#
# def twoSum(List,target):
#
#     ls = []
#
#     for i in range(0, len(List)):
#
#         for j in range(0, len(List)):
#             if List[i] + List[j] == target:
#                 ls.append(i + 1)
#                 ls.append(j + 1)
#             else:
#                 continue
#     ls = list(set(ls))
#
#     return ls
#
# nums = [2,3,4]
# target = 6
# print(twoSum(nums,target))


#OR


def twoSum(array,target):

    array.sort()
    left = 0
    right = len(array) - 1
    a = []

    while (left < right):

        currentSum = array[left] + array[right]

        if currentSum == target:
            a.append(array[left])
            a.append(array[right])
            return a
        elif currentSum < target:
            left += 1
        elif currentSum > target:
            right -= 1

    return []






a = [3,4,1,0,2]
target = 9

print(twoSum(a,target))



