class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        
        for i in range(len(nums)):
            a = nums[i]
            b = target - a
            
            if b in cache: 
                return [i, cache[b]]
            
            else: 
                cache[a] = i