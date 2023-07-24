class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        az = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        az_dict = {letter: index + 1 for index, letter in enumerate(az)}
        ans = 0
        
        for title in columnTitle:
            ans = ans * 26 + az_dict[title]
                        
        return ans
