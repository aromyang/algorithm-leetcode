# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        self.ans = []
        to_delete = set(to_delete)
        
        def dfs(cur_node, new_root):
            if not cur_node:
                return None
            
            cur_deleted = cur_node.val in to_delete
        
            if new_root and not cur_deleted:
                self.ans.append(cur_node)
            
            cur_node.left = dfs(cur_node.left, cur_deleted)
            cur_node.right = dfs(cur_node.right, cur_deleted)
            
            return None if cur_deleted else cur_node
                
        dfs(root, True)
        
        return self.ans