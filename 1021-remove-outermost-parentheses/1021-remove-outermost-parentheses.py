class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        answer = ""
        stack = []
        primitive = []
        
        for ss in s:
            primitive.append(ss)
            if ss == '(':
                stack.append('(')
            else:
                stack.pop()
                if not stack:
                    answer += ''.join(primitive[1:-1])
                    primitive.clear()
        
        return answer