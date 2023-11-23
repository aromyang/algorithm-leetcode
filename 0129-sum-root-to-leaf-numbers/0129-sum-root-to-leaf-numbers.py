# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(cur_node, path):
            if not cur_node:
                return
            
            if cur_node.left:
                dfs(cur_node.left, path + str(cur_node.left.val))
            if cur_node.right:
                dfs(cur_node.right, path + str(cur_node.right.val))
            
            if not cur_node.left and not cur_node.right:
                self.ans += int(path)            
        
        dfs(root, str(root.val))
        
        return self.ans