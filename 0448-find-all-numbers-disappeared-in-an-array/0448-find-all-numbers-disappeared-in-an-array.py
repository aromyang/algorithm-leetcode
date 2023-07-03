class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        integers = set([x for x in range(1, len(nums) + 1)])
        for num in nums:
            integers.discard(num)
        
        return list(integers)