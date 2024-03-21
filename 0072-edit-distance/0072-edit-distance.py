class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1, len2 = len(word1), len(word2)
        dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
        
        for l1 in range(len1 + 1):
            dp[l1][0] = l1
        for l2 in range(len2 + 1):
            dp[0][l2] = l2
            
        for l1 in range(1, len1 + 1):
            for l2 in range(1, len2 + 1):
                if word1[l1-1] == word2[l2-1]:
                    dp[l1][l2] = dp[l1-1][l2-1]
                else:
                    dp[l1][l2] = 1 + min(
                        dp[l1-1][l2],
                        dp[l1][l2-1],
                        dp[l1-1][l2-1]
                    )
        
        return dp[len1][len2]