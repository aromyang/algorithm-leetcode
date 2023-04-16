"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        ans = [root.val]
        
        def traversal(root):
            if len(root.children) == 0:
                return
            for i in range(len(root.children)):
                ans.append(root.children[i].val)
                traversal(root.children[i])
            
        traversal(root)   
        return ans
