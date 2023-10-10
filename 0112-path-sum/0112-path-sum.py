# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(cur_node, cur_sum):
            if cur_node is None:
                return False
            
            cur_sum += cur_node.val
            
            if cur_node.left is None and cur_node.right is None:
                return cur_sum == targetSum
            
            return dfs(cur_node.left, cur_sum) or dfs(cur_node.right, cur_sum)
        
        return root and dfs(root, 0)