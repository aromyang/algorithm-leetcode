class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dp(i):
            if i < 0:
                return 0
            if i in memo:
                return memo[i]
            
            result = max(dp(i - 2) + nums[i], dp(i - 1))
            memo[i] = result
            return result

        return dp(len(nums) - 1)
