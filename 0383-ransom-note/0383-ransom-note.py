class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote):
            return False
        
        goal = {}
        
        for r in ransomNote:
            goal[r] = 1 + goal.get(r, 0)
        
        for m in magazine:
            if not goal:
                return True
            if m in goal:
                goal[m] = goal.get(m) - 1
                if goal[m] == 0:
                    del goal[m]
        
        return not goal