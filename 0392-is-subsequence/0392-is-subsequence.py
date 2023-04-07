class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if len(s) > len(t):
            return False
        idx = 0
        for tt in t:
            if tt == s[idx]:
                idx += 1
            if idx == len(s):
                return True
        return False