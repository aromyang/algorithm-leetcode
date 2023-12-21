class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        limit_x, limit_y = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = [[False] * limit_y for _ in range(limit_x)]
        ans = 0
        
        def bfs(start_x, start_y):
            if grid[start_x][start_y] == 1:
                return True
            
            q = deque([(start_x, start_y)])
            is_island = True

            while q:
                cur_x, cur_y = q.popleft()
                if cur_x == 0 or cur_x == limit_x - 1 or cur_y == 0 or cur_y == limit_y - 1:
                    if grid[cur_x][cur_y] == 0:
                        is_island = False

                for dx, dy in directions:
                    next_x, next_y = cur_x + dx, cur_y + dy
                    if 0 <= next_x < limit_x and 0 <= next_y < limit_y:
                        if not visited[next_x][next_y] and grid[next_x][next_y] == 0:
                            visited[next_x][next_y] = True
                            q.append((next_x, next_y))

            return 1 if is_island else 0
                                
        for x in range(limit_x):
            for y in range(limit_y):
                if not visited[x][y] and grid[x][y] == 0:
                    visited[x][y] = True
                    ans += bfs(x, y)
        
        return ans