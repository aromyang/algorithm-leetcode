class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        nums_set = set(nums)
        
        def backtrack(current):
            if len(current) == n:
                if current not in nums_set:
                    return current
                return None
        
            ans = backtrack(current + '0')
            if ans is not None:
                return ans
            
            ans = backtrack(current + '1')
            if ans is not None:
                return ans
            
            return None
        
        return backtrack('')