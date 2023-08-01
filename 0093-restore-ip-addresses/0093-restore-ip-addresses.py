class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        anss = []
        
        if len(s) < 4 or len(s) > 12:
            return anss
        
        def backtrack(s, ans):
            if len(ans) == 4:
                if not s:
                    anss.append('.'.join(ans))
                return
            
            for i in range(min(3, len(s))):
                part = s[:i+1]
                if (part == '0' or not part.startswith('0')) and 0 <= int(part) <= 255:
                    backtrack(s[i+1:], ans + [part])
        
        backtrack(s, [])
    
        return anss