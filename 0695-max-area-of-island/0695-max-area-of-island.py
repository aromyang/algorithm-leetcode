class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.ans = 0
        limit_x, limit_y = len(grid), len(grid[0])
        visited = [[False] * limit_y for _ in range(limit_x)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def dfs(cur_x, cur_y):
            if visited[cur_x][cur_y] or grid[cur_x][cur_y] == 0:
                return 0
            
            visited[cur_x][cur_y] = True
            area = 1
            
            for dx, dy in directions:
                next_x, next_y = cur_x + dx, cur_y + dy
                if 0 <= next_x < limit_x and 0 <= next_y< limit_y:
                    area += dfs(next_x, next_y)
                    
            return area
        
        for x in range(limit_x):
            for y in range(limit_y):
                if not visited[x][y] and grid[x][y] == 1:
                    area = dfs(x, y)
                    self.ans = max(area, self.ans)
        
        return self.ans
                
        