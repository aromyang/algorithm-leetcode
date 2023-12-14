# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        ans = root.val
        max_depth = 0
        q = deque([(root, max_depth)])
        
        while q:
            cur_node, cur_depth = q.popleft()
            
            if cur_depth > max_depth:
                ans = cur_node.val
                max_depth = cur_depth
            
            if cur_node.left:
                q.append((cur_node.left, cur_depth + 1))
            if cur_node.right:
                q.append((cur_node.right, cur_depth + 1))
        
        return ans