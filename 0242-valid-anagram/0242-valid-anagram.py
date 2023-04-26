class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        need = {}
        for ss in s:
            need[ss] = need.get(ss, 0) + 1

        for tt in t:
            if tt not in need or need[tt] <= 0:
                return False
            if tt in need:
                need[tt] = need.get(tt) - 1

        return True