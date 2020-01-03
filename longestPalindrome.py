
import collections

def longestPalindrome(ls):

    odds = sum(v & 1 for v in ls)
    return len(ls) - odds + bool(odds)

ls = [1,1,4,2]
print(longestPalindrome(ls))