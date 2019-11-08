

#one of the sorting technique

# time - O(n^2)
# space - O(1)


def bubbleSort(array):


    for i in range(0,len(array)):
        left = array[i]
        for j in range(i+1,len(array)-1):
            if left > array[j]:
                temp = array[left]
                array[left] = array[j]
                array[j] = temp
            else:
                continue

    return array





array = [9,4,2,6,5,7,1,3,8]
print(bubbleSort(array))
