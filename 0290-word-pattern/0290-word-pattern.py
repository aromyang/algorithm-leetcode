class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        strs = s.split()
        if len(pattern) != len(strs):
            return False
        
        patt = {}
        reverse_patt = {}
        
        for i in range(len(pattern)):
            if pattern[i] not in patt:
                patt[pattern[i]] = strs[i]
            elif patt.get(pattern[i]) != strs[i]:
                return False
            
            if strs[i] not in reverse_patt:
                reverse_patt[strs[i]] = pattern[i]
            elif reverse_patt.get(strs[i]) != pattern[i]:
                return False
            
        return True