class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        n = len(pressedKeys)
        mod = 10**9 + 7 
        max_press = {str(k): 4 if k in [7, 9] else 3 for k in range(2, 10)}
        
        dp = [0] * (n+1)
        dp[0] = 1  
        
        for i in range(1, n+1):
            dp[i] = dp[i-1]  
            cur_key = pressedKeys[i-1]
            
            for j in range(2, max_press[cur_key] + 1):
                if i-j < 0: 
                    break 
                if pressedKeys[i-j] != cur_key: 
                    break 
                    
                dp[i] = (dp[i] + dp[i-j]) % mod 
            
        return dp[-1]
