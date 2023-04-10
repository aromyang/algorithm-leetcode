# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> ListNode:
        if not list1 or not list2:
            return list1 or list2
        
        def create_node(val):
            return ListNode(val=val, next=None)
        
        def add_node(node, val):
            new_node = create_node(val)
            node.next = new_node
            return new_node

        ans = None
        cur = None

        while list1 or list2:
            if not list1:
                cur.next = list2
                break
            elif not list2:
                cur.next = list1
                break
            elif list1.val <= list2.val:
                if not ans:
                    ans = create_node(list1.val)
                    cur = ans
                else:
                    cur = add_node(cur, list1.val)
                list1 = list1.next
            else:
                if not ans:
                    ans = create_node(list2.val)
                    cur = ans
                else:
                    cur = add_node(cur, list2.val)
                list2 = list2.next
        return ans

                