class Solution:
    def countArrangement(self, n: int) -> int:
        def backtrack(idx, visited):
            if idx > n:
                return 1
            
            cnt = 0
            for i in range(1, n + 1):
                if not visited[i] and not (i % idx and idx % i):
                    visited[i] = True
                    cnt += backtrack(idx + 1, visited)
                    visited[i] = False
            
            return cnt
        
        visited = [False] * (n + 1)
        
        return backtrack(1, visited)