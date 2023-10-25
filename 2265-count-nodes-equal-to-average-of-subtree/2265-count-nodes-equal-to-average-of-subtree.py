# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(cur_node):
            if not cur_node:
                return (0, 0)
                        
            left_val, left_children = dfs(cur_node.left)
            right_val, right_children = dfs(cur_node.right)
            
            cur_val = left_val + right_val + cur_node.val
            cur_children = left_children + right_children + 1
            
            cur_avg = cur_val // cur_children
            if cur_node.val == cur_avg:
                self.ans += 1
            
            return (cur_val, cur_children)
        
            
        dfs(root)
        
        return self.ans