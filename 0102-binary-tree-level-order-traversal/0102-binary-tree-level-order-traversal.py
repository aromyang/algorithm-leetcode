# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque()
        queue.append(root)
        ans = []
        
        while queue:
            levels = len(queue)
            cur_level = []
            
            for _ in range(levels):
                cur_node = queue.popleft()
                cur_level.append(cur_node.val)
                
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
            
            ans.append(cur_level)
        
        return ans