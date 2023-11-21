class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        limit_x, limit_y = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = [[False] * limit_y for _ in range(limit_x)]
        ans = 0
        
        def dfs(cur_x, cur_y):
            if cur_x == 0 or cur_x == limit_x - 1 or cur_y == 0 or cur_y == limit_y - 1:
                if grid[cur_x][cur_y] == 0:
                    return False
            
            if grid[cur_x][cur_y] == 1 or visited[cur_x][cur_y]:
                return True
            
            visited[cur_x][cur_y] = True
            is_islands = True
            
            for dx, dy in directions:
                next_x, next_y = cur_x + dx, cur_y + dy
                if 0 <= next_x < limit_x and 0 <= next_y < limit_y:
                    is_islands &= dfs(next_x, next_y)
                        
            return is_islands
                                
        for x in range(limit_x):
            for y in range(limit_y):
                if not visited[x][y] and grid[x][y] == 0:
                    if dfs(x, y):
                        ans += 1
        
        return ans