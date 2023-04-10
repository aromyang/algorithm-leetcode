# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> ListNode:    
        if not list1 or not list2:
            return list1 or list2

        ans = None

        while list1 or list2:
            if not list1:
                cur = ans
                while cur.next:
                    cur = cur.next
                cur.next = list2
                return ans
            elif not list2:
                cur = ans
                while cur.next:
                    cur = cur.next
                cur.next = list1
                return ans
            if list1.val <= list2.val:
                if not ans:
                    ans = ListNode(val=list1.val, next=None)
                else:
                    cur = ans
                    while cur.next:
                        cur = cur.next
                    cur.next = ListNode(val=list1.val, next=None)
                list1 = list1.next
            else:
                if not ans:
                    ans = ListNode(val=list2.val, next=None)
                else:
                    cur = ans
                    while cur.next:
                        cur = cur.next
                    cur.next = ListNode(val=list2.val, next=None)
                list2 = list2.next
        return ans

                