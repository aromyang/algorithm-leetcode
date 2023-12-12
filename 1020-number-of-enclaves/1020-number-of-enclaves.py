class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        limit_x, limit_y = len(grid), len(grid[0])
        
        if limit_y == 1 or limit_y == 1:
            return 0
        
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = [[False] * limit_y for _ in range(limit_x)]
        
        self.q = deque()
        ans = 0
        
        def bfs():
            cells = 0
            can_walk = True
                        
            while self.q:
                cells += 1
                cur_x, cur_y = self.q.popleft()
                
                if cur_x == 0 or cur_x == limit_x - 1 or cur_y == 0 or cur_y == limit_y - 1:
                    can_walk = False
                
                for dx, dy in directions:
                    next_x, next_y = cur_x + dx, cur_y + dy
                    if 0 <= next_x < limit_x and 0 <= next_y < limit_y:
                        if not visited[next_x][next_y] and grid[next_x][next_y] == 1:
                            if next_x == 0 or next_x == limit_x - 1 or next_y == 0 or next_y == limit_y - 1:
                                can_walk = False
                            visited[next_x][next_y] = True
                            self.q.append((next_x, next_y))
                            
            return cells if can_walk else 0
                
        for x in range(limit_x):
            for y in range(limit_y):
                if grid[x][y] == 1 and not visited[x][y]:
                    visited[x][y] = True
                    self.q.append((x, y))
                    ans += bfs()
                    
        return ans