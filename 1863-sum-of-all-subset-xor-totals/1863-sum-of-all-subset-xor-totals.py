class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        
        for mask in range(1 << n):
            cur_xor_subset = 0
            for idx in range(n):
                if mask & (1 << idx):
                    cur_xor_subset ^= nums[idx]
            ans += cur_xor_subset
        
        return ans