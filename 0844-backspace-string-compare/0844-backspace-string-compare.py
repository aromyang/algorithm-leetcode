class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def backspace(st: str) -> List[str]:
            stack = []
            for stst in st:
                if stst == '#' and stack:
                    stack.pop()
                elif stst != '#':
                    stack.append(stst)
            return stack
                        
        return backspace(s) == backspace(t)
