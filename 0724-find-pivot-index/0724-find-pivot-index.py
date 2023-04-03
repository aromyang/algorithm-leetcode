class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        nums_sum = [nums[0]]
        last = len(nums) - 1

        for i in range(1, last + 1):
            nums_sum.append(nums_sum[i - 1] + nums[i])

        if nums_sum[last] - nums_sum[0] == 0:
            return 0
        
        for pivot in range(1, last):
            if nums_sum[pivot - 1] == nums_sum[last] - nums_sum[pivot]:
                return pivot
            
        if nums_sum[last - 1] == 0:
            return last

        return -1