class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) <= 10:
            return []
        
        ans = {}
        for i in range(len(s) - 9):
            cur = s[i:i+10]
            ans[cur] = ans.get(cur, 0) + 1
                
        return [k for k, v in ans.items() if v > 1]