class Solution:
    def tribonacci(self, n: int) -> int:
        ans = {}
        ans[0] = 0
        ans[1] = 1
        ans[2] = 1
        
        if n in ans:
            return ans[n]
        
        for i in range(3, n + 1):
            ans[i] = ans.get(i - 3) + ans.get(i - 2) + ans.get(i - 1)
        
        return ans[n]