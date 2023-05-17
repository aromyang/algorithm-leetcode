class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for ss in s:
            if stack and stack[-1] == ss:
                stack.pop()
            else:
                stack.append(ss)
        
        return ''.join(stack)