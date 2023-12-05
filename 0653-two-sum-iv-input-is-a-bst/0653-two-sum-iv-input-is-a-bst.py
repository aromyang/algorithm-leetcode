# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()
        q = deque([root])
        
        while q:
            cur_node = q.popleft()
            
            if k - cur_node.val in seen:
                return True
            
            seen.add(cur_node.val)
            
            if cur_node.left:
                q.append(cur_node.left)
            if cur_node.right:
                q.append(cur_node.right)
        
        return False