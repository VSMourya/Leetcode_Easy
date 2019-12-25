#
# Question
# Given head which is a reference node to a singly-linked list.
# The value of each node in the linked list is either 0 or 1.
# The linked list holds the binary representation of a number.
# Return the decimal value of the number in the linked list.

# Input: head = [1,0,1]
# Output: 5
# Explanation: (101) in base 2 = (5) in base 10


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:

        head1 = head
        count = -1

        while head1:
            count += 1
            head1 = head1.next

        res = 0

        while head != None:
            res += head.val*(2**(count))
            head = head.next
            count -= 1

        return res


        # OR
        #
        # output = 0
        # while head:
        #     output = 2*output + head.val
        #     head = head.next
        # return output