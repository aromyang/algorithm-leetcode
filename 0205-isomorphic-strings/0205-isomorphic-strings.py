class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        convert = {}
        used = set()
        for i in range(len(s)):
            if s[i] in convert:
                if convert.get(s[i]) != t[i]:
                    return False
            else:
                if t[i] in used:
                    return False
                convert[s[i]] = t[i]
                used.add(t[i])
        return True