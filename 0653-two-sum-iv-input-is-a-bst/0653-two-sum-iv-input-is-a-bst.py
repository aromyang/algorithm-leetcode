# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def dfs(cur_node, visited):
            if cur_node is None:
                return False
            
            if k - cur_node.val in visited:
                return True
            
            visited.add(cur_node.val)
            
            return dfs(cur_node.left, visited) or dfs(cur_node.right, visited)
        
        return dfs(root, set())