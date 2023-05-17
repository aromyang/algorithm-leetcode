class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        answer = 0
        for ss in s:
            if ss == '(':
                stack.append(ss)
            elif ss == ')':
                answer = max(len(stack), answer)
                stack.pop()
        
        return answer
                