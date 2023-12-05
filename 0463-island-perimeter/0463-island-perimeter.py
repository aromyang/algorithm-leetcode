class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0
        x_limit, y_limit = len(grid), len(grid[0])
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        q = deque()
        
        for x in range(x_limit):
            for y in range(y_limit):
                if grid[x][y] == 1:
                    visited[x][y] = True
                    q.append((x, y))
                    
                    while q:
                        cur_x, cur_y = q.popleft()

                        for dx, dy in directions:
                            next_x, next_y = cur_x + dx, cur_y + dy
                            if 0 <= next_x < x_limit and 0 <= next_y < y_limit:
                                if grid[next_x][next_y] == 1:
                                    if not visited[next_x][next_y]:
                                        visited[next_x][next_y] = True
                                        q.append((next_x, next_y))
                                    ans -= 1
                        
                        ans += 4

                    return ans