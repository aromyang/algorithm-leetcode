# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q = deque([(root, 1)])
        depth_sum = defaultdict(int)
        
        while q:
            cur_node, depth = q.popleft()
            depth_sum[depth] += cur_node.val
            
            if cur_node.left:
                q.append((cur_node.left, depth + 1))
            if cur_node.right:
                q.append((cur_node.right, depth + 1))
        
        return depth_sum[max(depth_sum.keys())]