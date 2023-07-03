class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = Counter(nums).most_common(1)
        return ans[0][0]