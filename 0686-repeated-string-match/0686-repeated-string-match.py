class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if len(set(a)) < len(set(b)):
            return -1
        if b in a:
            return 1
        
        min_start = len(b) // len(a)
        for i in range(min_start, min_start + 3):
            cur = a * i
            if b in cur:
                return i
        
        return -1