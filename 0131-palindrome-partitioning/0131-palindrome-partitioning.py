class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def is_palindrome(start, end):
            if dp[start][end] is not None:
                return dp[start][end]
            l, r = start, end
            while l < r:
                if s[l] != s[r]:
                    dp[start][end] = False
                    return False
                l += 1
                r -= 1
            dp[start][end] = True
            return True
        
        def dfs(start, path):
            if start == len(s):
                ans.append(path)
                return
            for end in range(start, len(s)):
                if is_palindrome(start, end):
                    dfs(end + 1, path + [s[start:end+1]])
            
        dp = [[None] * len(s) for _ in range(len(s))]
        ans = []
        dfs(0, [])
        
        return ans