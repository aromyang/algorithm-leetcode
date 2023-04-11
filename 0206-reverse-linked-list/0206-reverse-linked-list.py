# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        linked = []
        cur = head
        while cur:
            linked.append(ListNode(val=cur.val))
            cur = cur.next
                
        reversed_nodes = list(reversed(linked))
        print(reversed_nodes)
        new_head = reversed_nodes[0]
        new_cur = new_head
        for i in range(1, len(reversed_nodes)):
            new_cur.next = reversed_nodes[i]
            new_cur = new_cur.next        
        
        return new_head