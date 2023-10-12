class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        x_limit, y_limit = len(grid), len(grid[0])
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        ans = 0
        
        def dfs(cur_x, cur_y):
            nonlocal ans
            visited[cur_x][cur_y] = True
            for dx, dy in directions:
                next_x, next_y = cur_x + dx, cur_y + dy
                if 0 <= next_x < x_limit and 0 <= next_y < y_limit:
                    if grid[next_x][next_y] == 1 and not visited[next_x][next_y]:
                        dfs(next_x, next_y)
                    elif grid[next_x][next_y] == 0:
                        ans += 1
                else:
                    ans += 1
                        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    dfs(x, y)
                    return ans