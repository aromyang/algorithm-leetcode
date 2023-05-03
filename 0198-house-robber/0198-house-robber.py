class Solution:
    def rob(self, nums: List[int]) -> int:
        houses = len(nums)
        memo = {}
        memo[0] = 0
        memo[1] = nums[0]

        for i in range(2, houses + 1):
            memo[i] = max(memo[i - 1], memo[i - 2] + nums[i - 1])

        return memo[houses]
