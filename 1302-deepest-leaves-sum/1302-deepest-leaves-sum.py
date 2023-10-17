# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        self.max_depth = 1
        self.ans = 0
        
        def dfs(cur_node, cur_depth):            
            if not cur_node:
                return
            
            cur_depth += 1
            
            if cur_depth > self.max_depth:
                self.ans = cur_node.val
            elif cur_depth == self.max_depth:
                self.ans += cur_node.val
            
            self.max_depth = max(self.max_depth, cur_depth)
            
            dfs(cur_node.left, cur_depth)
            dfs(cur_node.right, cur_depth)
        
        dfs(root, 0)
        
        return self.ans