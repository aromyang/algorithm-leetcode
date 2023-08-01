class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        ans = ['' for _ in range(numRows)]        
        row = 0
        direction = -1
        
        for ss in s:
            ans[row] += ss
            
            if row == 0 or row == numRows - 1:
                direction *= -1
            
            row += direction

        return ''.join(ans)