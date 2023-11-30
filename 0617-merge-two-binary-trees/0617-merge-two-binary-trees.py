# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 or not root2:
            return root1 or root2
        
        q1 = deque()
        q2 = deque()
        q1.append(root1)
        q2.append(root2)
        
        while q1 and q2:
            node1 = q1.popleft()
            node2 = q2.popleft()
            
            node1.val += node2.val
            
            if node1.left and node2.left:
                q1.append(node1.left)
                q2.append(node2.left)
            elif not node1.left and node2.left:
                node1.left = node2.left
            
            if node1.right and node2.right:
                q1.append(node1.right)
                q2.append(node2.right)
            elif not node1.right and node2.right:
                node1.right = node2.right
            
        return root1
