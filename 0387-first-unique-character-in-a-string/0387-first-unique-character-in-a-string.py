class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i, ss in enumerate(s):
            if s.index(ss) == s.rindex(ss):
                return i
        
        return -1