class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n <= 2:
            return 1
        if n == 3:
            return 2
        
        left, right = 1, n // 2
        
        while left <= right:
            row = (left + right) // 2
            need = (row * (row + 1)) // 2
            if need == n:
                return row
            elif need < n:
                left = row + 1
            else:
                right = row - 1
        
        return right