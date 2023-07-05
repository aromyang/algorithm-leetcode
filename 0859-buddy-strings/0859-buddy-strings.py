class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        diff = []
        cnt = {}
        
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff.append((s[i], goal[i]))
            cnt[s[i]] = cnt.get(s[i], 0) + 1
            
        if len(diff) == 2 and diff[0] == diff[1][::-1]:
            return True
    
        if len(diff) == 0 and max(cnt.values()) >= 2:
            return True
        
        return False