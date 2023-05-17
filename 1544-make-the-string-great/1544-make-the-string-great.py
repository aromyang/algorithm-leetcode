class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        
        for ss in s:
            if stack and stack[-1].lower() == ss.lower() and stack[-1] != ss:
                stack.pop()
            else:
                stack.append(ss)
        
        return ''.join(stack)