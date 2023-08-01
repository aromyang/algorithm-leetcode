class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        ans = [[] for i in range(numRows)]        
        row = 0
        app = 1
        for ss in s:
            if row == numRows - 1:
                app = -1
            if row == 0:
                app = 1
            ans[row].append(ss)
            row += app

        return ''.join([''.join(row) for row in ans])