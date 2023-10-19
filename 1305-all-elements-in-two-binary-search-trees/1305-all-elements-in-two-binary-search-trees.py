# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        ans = []
        
        def dfs(cur_node):
            if not cur_node:
                return
            
            ans.append(cur_node.val)
            
            dfs(cur_node.left)
            dfs(cur_node.right)
        
        
        dfs(root1)
        dfs(root2)
        
        ans.sort()
        
        return ans