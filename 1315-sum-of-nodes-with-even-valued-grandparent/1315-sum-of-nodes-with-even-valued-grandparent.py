# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        ans = 0
        q = deque([(root, False, False)])
        
        while q:
            cur_node, parent, g_parent = q.popleft()
            
            if g_parent:
                ans += cur_node.val
            
            parent, g_parent = cur_node.val & 1 == 0, parent
            
            if cur_node.left:
                q.append((cur_node.left, parent, g_parent))
            if cur_node.right:
                q.append((cur_node.right, parent, g_parent))
            
            
        return ans