


# leetcode 1207
# Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.
#
# Example 1:
# Input: arr = [1,2,2,1,1,3]
# Output: true
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
#

def uniqueOccurrences(arr):

    hsh = {}

    for i in arr:
        if i in hsh:
            hsh[i] += 1
        else:
            hsh[i] = 1

    vals = hsh.values()
    return len(vals) == len(set(vals))


arr = [1,2,2,1,1,3]
print(uniqueOccurrences(arr))