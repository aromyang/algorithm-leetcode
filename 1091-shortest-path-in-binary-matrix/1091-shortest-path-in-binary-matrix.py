class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        
        row = len(grid)
        col = len(grid[0])
        visited = [[False] * col for _ in range(row)]

        queue = deque()
        queue.append((0, 0, 1))
        visited[0][0] = True

        dx = [-1, 1, 0, 0, 1, 1, -1, -1]
        dy = [0, 0, -1, 1, -1, 1, -1, 1]

        while queue:
            cur_x, cur_y, cur_d = queue.popleft()            
            if cur_x == row - 1 and cur_y == col - 1:
                return cur_d

            for d in range(len(dx)):
                next_x = cur_x + dx[d]
                next_y = cur_y + dy[d]
                if 0 <= next_x < row and 0 <= next_y < col:
                    if not visited[next_x][next_y] and grid[next_x][next_y] == 0:
                        queue.append((next_x, next_y, cur_d + 1))
                        visited[next_x][next_y] = True
        return -1
                                