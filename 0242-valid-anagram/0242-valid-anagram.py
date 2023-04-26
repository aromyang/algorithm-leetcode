class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sorted_s = ''.join(sorted(s, key=lambda x: x.lower()))
        sorted_t = ''.join(sorted(t, key=lambda x: x.lower()))
        
        return sorted_s == sorted_t