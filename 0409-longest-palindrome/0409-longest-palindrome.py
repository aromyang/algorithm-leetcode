class Solution:
    def longestPalindrome(self, s: str) -> int:
        nums = {}
        for ss in s:
            nums[ss] = 1 + nums.get(ss, 0)
                
        palindrome = 0
        has_odd = False
        for value in nums.values():
            if value & 1: 
                has_odd = True
                palindrome += (value - 1)
            else:
                palindrome += value
        
        return palindrome + 1 if has_odd else palindrome