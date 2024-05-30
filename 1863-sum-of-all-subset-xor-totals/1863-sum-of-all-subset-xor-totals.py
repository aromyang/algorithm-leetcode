class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def backtrack(idx, cur_xor):
            if idx == len(nums):
                return cur_xor
            
            include = backtrack(idx + 1, cur_xor ^ nums[idx])
            exclude = backtrack(idx + 1, cur_xor)
            
            return include + exclude
        
        return backtrack(0, 0)