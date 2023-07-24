class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ans = []
        idx1, idx2 = len(num1) - 1, len(num2) - 1
        go = 0
        
        while idx1 >= 0 or idx2 >= 0 or go:
            n1 = int(num1[idx1]) if idx1 >= 0 else 0
            n2 = int(num2[idx2]) if idx2 >= 0 else 0
            go, cur = divmod(n1 + n2 + go, 10)
            ans.append(str(cur))
            idx1 -= 1
            idx2 -= 1
        
        return ''.join(ans[::-1])