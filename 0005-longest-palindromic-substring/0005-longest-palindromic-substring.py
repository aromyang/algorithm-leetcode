class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        
        dp = [[False] * n for _ in range(n)]
        max_start, max_len = 0, 1
        
        for i in range(n):
            dp[i][i] = True
            
        for end in range(1, n):
            for start in range(end):
                is_same_char = s[end] == s[start]
                has_inner_palindrome = dp[start+1][end-1] or end - start == 1
                
                if is_same_char and has_inner_palindrome:
                    dp[start][end] = True
                    cur_len = end - start + 1
                    if cur_len > max_len:
                        max_start, max_len = start, cur_len
                        
                    if max_len == n:
                        return s
        
        return s[max_start:max_start+max_len]