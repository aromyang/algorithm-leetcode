# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        avgs = {}
        
        def dfs(cur_node, cur_level):
            if cur_node is None:
                return
            
            if cur_level not in avgs:
                avgs[cur_level] = [0, 0]
            
            avgs[cur_level][0] += cur_node.val
            avgs[cur_level][1] += 1
            
            dfs(cur_node.left, cur_level + 1)
            dfs(cur_node.right, cur_level + 1)
                
        
        dfs(root, 0)
        
        return [level_sum / level_cnt for level_sum, level_cnt in avgs.values()]