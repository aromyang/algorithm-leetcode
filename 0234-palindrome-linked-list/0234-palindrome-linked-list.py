# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.left = []
        self.right = []
        self.total_cnt = 0
        
        def recur(cur, cnt):
            if not cur:
                self.total_cnt = cnt - 1
                return
            
            recur(cur.next, cnt + 1)
            
            if cnt > self.total_cnt // 2:
                self.right.append(cur.val)
            else:
                self.left.append(cur.val)
        
        recur(head, 1)
        
        if self.total_cnt & 1:
            self.right = self.right[:-1]
        
        return self.left[::-1] == self.right