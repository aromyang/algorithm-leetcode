# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        ans = True
        
        while q:
            cur_node = q.popleft()
            if cur_node.left:
                if cur_node.val != cur_node.left.val:
                    return False
                q.append(cur_node.left)
            if cur_node.right:
                if cur_node.val != cur_node.right.val:
                    return False
                q.append(cur_node.right)
            
        return ans