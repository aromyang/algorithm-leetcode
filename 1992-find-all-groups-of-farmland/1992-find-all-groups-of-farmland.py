class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        ans = []
        self.q = deque()
        self.x_limit, self.y_limit = len(land), len(land[0])
        visited = [[False] * self.y_limit for _ in range(self.x_limit)]
        directions = [(1, 0), (0, 1)]
        
        def bfs(farmland):
            bottom_right = []
            while self.q:
                cur_x, cur_y = self.q.popleft()
                for dx, dy in directions:
                    next_x, next_y = cur_x + dx, cur_y + dy
                    if 0 <= next_x < self.x_limit and 0 <= next_y < self.y_limit:
                        if not visited[next_x][next_y] and land[next_x][next_y] == 1:
                            visited[next_x][next_y] = True
                            bottom_right = [next_x, next_y]
                            self.q.append((next_x, next_y))
            
            if not bottom_right:
                bottom_right = farmland
            farmland.extend(bottom_right)
            
            return farmland
        
        for x in range(self.x_limit):
            for y in range(self.y_limit):
                if land[x][y] == 1 and not visited[x][y]:
                    visited[x][y] = True
                    self.q.append((x, y))
                    ans.append(bfs([x, y]))
        
        return ans