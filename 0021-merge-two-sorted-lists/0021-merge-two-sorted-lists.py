# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> ListNode:
        if not list1 or not list2:
            return list1 or list2

        def merge(list1, list2):
            if not list1 or not list2:
                return list1 or list2
            
            if list1.val <= list2.val:
                list1.next = merge(list1.next, list2)
                return list1
            else:
                list2.next = merge(list1, list2.next)
                return list2
                
        
        if list1.val <= list2.val:
            ans = list1
            list1 = list1.next
        else:
            ans = list2
            list2 = list2.next

        ans.next = merge(list1, list2)
        
        return ans

                