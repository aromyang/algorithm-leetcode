class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        min_n = len(nums) // 3
        ans = []
        
        for k, v in cnt.items():
            if v > min_n:
                ans.append(k)
        
        return ans