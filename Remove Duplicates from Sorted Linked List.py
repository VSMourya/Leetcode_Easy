
# question
#
# Given a sorted linked list, delete all duplicates such that each element appear only once.
#
# Example 1:
#
# Input: 1->1->2
# Output: 1->2
# Example 2:
#
# Input: 1->1->2->3->3
# Output: 1->2->3

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(head):
        if head is None:
            return
        first = head
        second = head.next

        while second != None:
            if first.val == second.val:
                first.next = second.next
                second = second.next
            else:
                first = first.next
                second = second.next

        return head