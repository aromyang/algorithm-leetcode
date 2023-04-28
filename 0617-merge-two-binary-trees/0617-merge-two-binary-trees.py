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
        
        new_node = TreeNode(val=root1.val + root2.val)
        
        def mergeNodes(node1, node2):
            if not node1 or not node2:
                return node1 or node2
            
            new_node = TreeNode(val=node1.val + node2.val)
            new_node.left = mergeNodes(node1.left, node2.left)
            new_node.right = mergeNodes(node1.right, node2.right)
            return new_node
        
        new_node.left = mergeNodes(root1.left, root2.left)
        new_node.right = mergeNodes(root1.right, root2.right)
        
        return new_node
