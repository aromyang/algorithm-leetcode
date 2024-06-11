class Solution:
    def smallestNumber(self, pattern: str) -> str:
        
        def backtrack(idx, path, used):
            if idx == len(pattern) + 1:
                return path
            
            for num in range(1, 10):
                str_num = str(num)
                
                if str_num in used:
                    continue
                
                if idx == 0 or (pattern[idx - 1] == 'I' and path[-1] < str_num) or (pattern[idx - 1] == 'D' and path[-1] > str_num):
                    ans = backtrack(idx + 1, path + str_num, used | {str_num})
                    if ans:
                        return ans
            
            return None
        
        return backtrack(0, "", set())