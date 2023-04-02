class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ss in s:
            if ss == '(':
                stack.append(')')
            elif ss == '{':
                stack.append('}')
            elif ss == '[':
                stack.append(']')
            elif not stack or stack.pop() != ss:
                return False
        return not stack
