# https://leetcode.com/problems/reverse-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        reverse = None
        current = None
        while head != None:
            current = reverse
            reverse = ListNode(head.val)
            reverse.next = current
            
            head = head.next
        
        return reverse
        
        
        
            
        