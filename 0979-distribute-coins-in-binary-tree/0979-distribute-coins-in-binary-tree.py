# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(cur_node):
            if not cur_node:
                return (0, 0)
            
            left_nodes, left_coins = dfs(cur_node.left)
            right_nodes, right_coins = dfs(cur_node.right)
            
            self.ans += abs(left_nodes - left_coins) + abs(right_nodes - right_coins)
            
            return (left_nodes + right_nodes + 1, left_coins + right_coins + cur_node.val)
            
        
        dfs(root)

        return self.ans