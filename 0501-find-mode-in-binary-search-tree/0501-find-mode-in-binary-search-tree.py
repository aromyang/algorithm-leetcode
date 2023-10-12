# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        ans = {}
        def dfs(cur_node):
            nonlocal ans
            
            if not cur_node:
                return
            
            ans[cur_node.val] = ans.get(cur_node.val, 0) + 1
            
            dfs(cur_node.left)
            dfs(cur_node.right)
        
        dfs(root)
        mode = max(ans.values())
            
        return [k for k, v in ans.items() if v == mode]