class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sums = []
        for i in range(len(nums)):
            cur = nums[i]
            sums.append(cur)
            for j in range(i+1, len(nums)):
                cur += nums[j]
                sums.append(cur)
                
        sums.sort()
        
        return sum(sums[left-1:right]) % (10 ** 9 + 7)