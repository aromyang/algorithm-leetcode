# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        q = deque([root])
        
        while q:
            len_q = len(q)
            sum_lv = 0
            cnt_lv = 0
            
            for _ in range(len_q):
                cur_node = q.popleft()
                if cur_node:
                    sum_lv += cur_node.val
                    cnt_lv += 1
                if cur_node.left:
                    q.append(cur_node.left)
                if cur_node.right:
                    q.append(cur_node.right)
                    
            ans.append(sum_lv / cnt_lv)
        
        return ans