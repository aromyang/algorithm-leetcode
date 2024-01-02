# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def removeRights(head):
            if not head.next:
                return head.val, head
            
            right_val, right_head = removeRights(head.next)
                    
            if head.val < right_val:
                return right_val, right_head
            else:
                head.next = right_head
                return max(head.val, right_val), head

        return removeRights(head)[1]
