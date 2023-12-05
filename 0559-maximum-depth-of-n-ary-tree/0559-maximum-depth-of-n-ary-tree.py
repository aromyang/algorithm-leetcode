"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        max_depth = 1
        q = deque()
        q.append((root, max_depth))
        
        while q:
            cur_node, cur_depth = q.popleft()
            max_depth = cur_depth
            
            for child in cur_node.children:
                q.append((child, cur_depth + 1))
        
        return max_depth