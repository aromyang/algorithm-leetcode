class Solution:
    memo = {1:1, 2:2}
    def climbStairs(self, n: int) -> int:
        for i in range(3, n+1):
            self.memo[i] = self.memo[i-1] + self.memo[i-2]
        
        return self.memo[n]