class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        
        left, right = 2, num // 2
        
        while left <= right:
            mid = left + (right - left) // 2
            cur = mid ** 2
            
            if cur == num:
                return True
            elif cur > num:
                right = mid - 1
            else:
                left = mid + 1
        
        return False