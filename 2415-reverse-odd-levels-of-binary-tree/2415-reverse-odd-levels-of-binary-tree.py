# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.depth_dict = defaultdict(list)
        
        def dfs(cur_node, cur_depth):
            if not cur_node:
                return
            
            if cur_depth & 1:
                self.depth_dict[cur_depth].append(cur_node)
            
            dfs(cur_node.left, cur_depth + 1)
            dfs(cur_node.right, cur_depth + 1)
        
        dfs(root, 0)
        
        for depth, nodes in self.depth_dict.items():
            reversed_val = [node.val for node in reversed(nodes)]
            for i, node in enumerate(nodes):
                node.val = reversed_val[i]
        
        return root