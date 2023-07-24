class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        az = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        ans = []
        
        while columnNumber > 0:
            columnNumber -= 1
            columnNumber, left = divmod(columnNumber, 26)
            ans.append(az[left])
                        
        return ''.join(ans[::-1])