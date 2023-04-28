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

        
        def makeNewTree(root1, root2, cur_node):
            if not root1 or not root2:
                return
                        
            if not root1.left or not root2.left:
                cur_node.left = root1.left or root2.left
            else:
                cur_node.left = TreeNode(val=root1.left.val + root2.left.val)
            
            if not root1.right or not root2.right:
                cur_node.right = root1.right or root2.right
            else:
                cur_node.right = TreeNode(val=root1.right.val + root2.right.val)
                
            makeNewTree(root1.left, root2.left, cur_node.left)
            makeNewTree(root1.right, root2.right, cur_node.right)
        
        makeNewTree(root1, root2, new_node)
        
        return new_node
    