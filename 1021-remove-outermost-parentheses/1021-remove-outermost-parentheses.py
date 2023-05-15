class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        answer = []
        stack = []
        start = 0
        
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if len(stack) == 1:
                    answer.append(s[start+1:i])
                    start = i + 1
                stack.pop()
                
        return ''.join(answer)