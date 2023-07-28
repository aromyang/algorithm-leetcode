class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                rm_left = s[:left] + s[left+1:]
                rm_right = s[:right] + s[right+1:]
                return rm_left == rm_left[::-1] or rm_right == rm_right[::-1]
                
            left += 1
            right -= 1
            
        return True