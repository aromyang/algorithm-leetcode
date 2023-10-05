"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        max_depth = 0
        
        if not root:
            return max_depth
        
        def dfs(cur_node, cur_depth):
            nonlocal max_depth
            if not cur_node.children:
                max_depth = max(max_depth, cur_depth + 1)
            for child in cur_node.children:
                dfs(child, cur_depth + 1)
        
        dfs(root, 0)
        
        return max_depth