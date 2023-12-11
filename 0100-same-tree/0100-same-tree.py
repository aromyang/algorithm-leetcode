# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if bool(p) != bool(q):
            return False
        
        if not p and not q:
            return True
        
        queue = deque([(p, q)])
        
        while queue:
            p_node, q_node = queue.popleft()
            if p_node.val != q_node.val:
                return False

            if bool(p_node.left) != bool(q_node.left) or bool(p_node.right) != bool(q_node.right):
                return False
            
            if p_node.left and q_node.left:
                queue.append((p_node.left, q_node.left))
            if p_node.right and q_node.right:
                queue.append((p_node.right, q_node.right))
            
        
        return True