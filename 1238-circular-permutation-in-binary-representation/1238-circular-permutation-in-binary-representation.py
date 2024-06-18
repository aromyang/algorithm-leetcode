class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        
        def backtrack(visited, path, prev_str, goal):
            if len(visited) == goal:
                return True
            
            for i in range(n):
                new_str = prev_str[:i] + str(1 - int(prev_str[i])) + prev_str[i + 1:]
                if new_str not in visited:
                    visited.add(new_str)
                    path.append(new_str)
                    
                    if backtrack(visited, path, new_str, goal):
                        return True
                    
                    visited.remove(new_str)
                    path.pop()
            return False
        
        sys.setrecursionlimit(1000000)
        
        visited = set()
        initial_str = bin(start)[2:].zfill(n)
        path = [initial_str]
        visited.add(initial_str)
        
        backtrack(visited, path, initial_str, 2 ** n)

        return [int(binary_str, 2) for binary_str in path]