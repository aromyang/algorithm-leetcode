# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(cur_node, depth):
            if cur_node is None:
                return 10 ** 5 + 1
            if not cur_node.left and not cur_node.right:
                return depth
            
            depth += 1
            
            return min(dfs(cur_node.left, depth), dfs(cur_node.right, depth))
        
        return dfs(root, 1) if root else 0