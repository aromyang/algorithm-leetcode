class Solution:
    def findLHS(self, nums: List[int]) -> int:
        cnts = Counter(nums)
        ans = 0

        for cnt in cnts:
            ans = max(ans, max(cnts.get(cnt) + cnts.get(cnt - 1, -cnts.get(cnt)), 
                               cnts.get(cnt) + cnts.get(cnt + 1, -cnts.get(cnt))))
            
        return ans