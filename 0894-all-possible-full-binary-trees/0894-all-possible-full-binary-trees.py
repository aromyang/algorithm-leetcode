# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        memo = {}

        def generateFBT(n: int) -> List[TreeNode]:
            if n in memo:
                return memo[n]

            if n % 2 == 0:
                return []

            if n == 1:
                return [TreeNode(0)]

            result = []
            for left_count in range(1, n, 2):
                right_count = n - 1 - left_count
                left_trees = generateFBT(left_count)
                right_trees = generateFBT(right_count)

                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(0)
                        root.left = left
                        root.right = right
                        result.append(root)

            memo[n] = result
            return result

        return generateFBT(n)
