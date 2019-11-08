
#Using two pointer technique (did it coz it was fun) ;)

def largestNumber(array):
    hsh = {}

    for i in array:
        if i not in hsh:
            hsh[i] = 1
        else:
            hsh[i] +=1

    arr = []
    for key,values in hsh.items():
        arr.append(key)
    print(arr)

    left = 0
    right = len(arr)-1
    while left <= right:

       if arr[left] > arr[right]:
           right-=1
       elif arr[left] < arr[right]:
           left+=1
       elif arr[left] == arr[right] and left == right:
           return arr[left]


arr = [3,5,94,234,1,4,43,12,45,11,234,94]

print(largestNumber(arr))


#
# OR
#
#
#
# largest = 0
#
# for i in arr:
#     if largest < i:
#         largest = i
#
# print(largest)