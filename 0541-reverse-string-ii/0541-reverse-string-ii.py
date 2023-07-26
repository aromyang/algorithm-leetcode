class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans = []
        for i in range(0, len(s), k*2):
            if len(s) - i < k:
                ans.append(s[i:i+k][::-1])
            elif len(s) - i < k*2:
                ans.append(s[i:i+k][::-1] + s[i+k:i+k*2])
            else:
                ans.append(s[i:i+k][::-1] + s[i+k:i+k*2])
        
        return ''.join(ans)