# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.subtrees = defaultdict(int)
        self.ans = []
        
        def dfs(cur_node):
            if not cur_node:
                return
            
            left = dfs(cur_node.left)
            right = dfs(cur_node.right)
            cur_subtree = (cur_node.val, left, right)
            
            if self.subtrees[cur_subtree] == 1:
                self.ans.append(cur_node)
            self.subtrees[cur_subtree] += 1
            
            return cur_subtree

            
        dfs(root)
        
        return self.ans