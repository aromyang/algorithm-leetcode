class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        ans[len(ans) - 1] = sum(nums)
        for i in range(len(nums) - 2, -1, -1):
            ans[i] = ans[i + 1] - nums[i + 1]
        return ans