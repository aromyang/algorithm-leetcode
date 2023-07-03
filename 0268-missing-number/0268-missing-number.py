class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        distinct = set([x for x in range(len(nums) + 1)])
        
        for num in nums:
            distinct.remove(num)
                
        return distinct.pop()