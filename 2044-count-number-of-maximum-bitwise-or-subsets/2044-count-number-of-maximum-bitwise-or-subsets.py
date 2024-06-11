class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        max_or = 0
        ans = 0
        
        for num in nums:
            max_or |= num
            
        
        def backtrack(idx, current_or):
            nonlocal max_or, ans
            
            if idx == n:
                if current_or == max_or:
                    ans += 1
                return
            
            backtrack(idx + 1, current_or | nums[idx])
            backtrack(idx + 1, current_or)
        
        
        backtrack(0, 0)
        
        return ans