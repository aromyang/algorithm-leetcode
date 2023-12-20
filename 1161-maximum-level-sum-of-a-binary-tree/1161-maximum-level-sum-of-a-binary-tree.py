# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        depth_dict = defaultdict(int)
        q = deque([(root, 1)])
        
        while q:
            cur_node, cur_depth = q.popleft()
            depth_dict[cur_depth] += cur_node.val
            
            if cur_node.left:
                q.append((cur_node.left, cur_depth + 1))
            if cur_node.right:
                q.append((cur_node.right, cur_depth + 1))
            
        
        return sorted(depth_dict.items(), key=lambda x:x[1], reverse=True)[0][0]