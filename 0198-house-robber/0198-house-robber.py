class Solution:
    def rob(self, nums: List[int]) -> int:
        houses = len(nums)
        
        if houses == 1:
            return nums[0]
        if houses == 2:
            return max(nums[0], nums[1])
        if houses == 3:
            return nums[2] + nums[0] if nums[2] + nums[0] >= max(nums) else max(nums)
        
        money = {}
        money[0] = nums[0]
        money[1] = max(nums[0], nums[1])
        money[2] = nums[2] + nums[0]
        
        
        for i in range(3, houses):
            money[i] = nums[i] + max(money[i - 2], money[i - 3])
        
        return max(money[houses - 1], money[houses - 2])