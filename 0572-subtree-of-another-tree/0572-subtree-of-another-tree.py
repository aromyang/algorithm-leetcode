# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_identical(cur_node, sub_node):
            if cur_node is None and sub_node is None:
                return True
            elif cur_node is None or sub_node is None:
                return False
            return cur_node.val == sub_node.val and is_identical(cur_node.left, sub_node.left) and is_identical(cur_node.right, sub_node.right)
        
        def dfs(cur_node):
            if cur_node is None:
                return False
            if is_identical(cur_node, subRoot):
                return True
            return dfs(cur_node.left) or dfs(cur_node.right)
        
        return dfs(root)