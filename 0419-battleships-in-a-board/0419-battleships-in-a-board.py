class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        x_limit, y_limit = len(board), len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[False] * y_limit for _ in range(x_limit)]
        
        def dfs(cur_x, cur_y):
            nonlocal x_limit, y_limit, directions, visited
            visited[cur_x][cur_y] = True
            
            for dx, dy in directions:
                next_x, next_y = cur_x + dx, cur_y + dy
                if 0 <= next_x < x_limit and 0 <= next_y < y_limit:
                    if board[next_x][next_y] == 'X' and not visited[next_x][next_y]:
                        dfs(next_x, next_y)
            
            
        ans = 0
        for x in range(x_limit):
            for y in range(y_limit):
                if board[x][y] == 'X' and not visited[x][y]:
                    dfs(x, y)
                    ans += 1
        
        return ans