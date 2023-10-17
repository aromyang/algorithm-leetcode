# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.gst = 0
        def dfs(cur_node):
            if not cur_node:
                return 0
            
            dfs(cur_node.right)
            cur_node.val += self.gst
            self.gst = cur_node.val
            dfs(cur_node.left)
            
            return cur_node.val
                
        dfs(root)
                
        return root