# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        ans = 0
        
        def dfs(cur_node, bit):
            nonlocal ans
            if cur_node.left is None and cur_node.right is None:
                bit += str(cur_node.val)
                ans += int(bit, 2)
            if cur_node.left:
                dfs(cur_node.left, bit + str(cur_node.val))
            if cur_node.right:
                dfs(cur_node.right, bit + str(cur_node.val))
        
        dfs(root, '')
        
        return ans