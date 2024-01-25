# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def findLength(head):
            length = 0
            while head:
                length += 1
                head = head.next
            return length
        
        def reorder(head, length):
            if length == 1:
                outTail = head.next
                head.next = None
                return outTail
            if length == 2:
                outTail = head.next.next
                head.next.next = None
                return outTail
            
            tail = reorder(head.next, length - 2)
            
            outTail = tail.next
            head.next, tail.next = tail, head.next
            return outTail
        
        if not head or not head.next or not head.next.next:
            return
        
        length = findLength(head)
        reorder(head, length)
