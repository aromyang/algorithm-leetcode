class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = Counter(s)
        stack = []
        
        for ss in s:
            counter[ss] -= 1
            if ss not in stack:
                while stack and ss < stack[-1] and counter[stack[-1]] > 0:
                    stack.pop()
                    
                stack.append(ss)
        
        
        return ''.join(stack)
        