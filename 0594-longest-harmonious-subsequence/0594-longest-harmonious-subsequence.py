class Solution:
    def findLHS(self, nums: List[int]) -> int:
        cnts = Counter(nums)
        ans = 0

        for cnt in cnts:
            if cnt + 1 in cnts:
                ans = max(ans, cnts.get(cnt) + cnts.get(cnt + 1))
            
        return ans