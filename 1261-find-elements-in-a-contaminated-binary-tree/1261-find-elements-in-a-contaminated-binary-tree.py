# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.elements = set()
        if not root: return
        
        root.val = 0
        q = deque([root])
        while q:
            cur_node = q.popleft()
            self.elements.add(cur_node.val)
            if cur_node.right:
                cur_node.right.val = 2 * cur_node.val + 2
                q.append(cur_node.right)
            if cur_node.left:
                cur_node.left.val = 2 * cur_node.val + 1
                q.append(cur_node.left)

    def find(self, target: int) -> bool:
        return True if target in self.elements else False


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)