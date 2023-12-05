class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        x_limit, y_limit = len(image), len(image[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = [[False] * y_limit for _ in range(x_limit)]
        
        q = deque([(sr, sc)])
        visited[sr][sc] = True
        target, image[sr][sc] = image[sr][sc], color
        
        while q:
            cur_x, cur_y = q.popleft()
            for dx, dy in directions:
                next_x, next_y = cur_x + dx, cur_y + dy
                if 0 <= next_x < x_limit and 0 <= next_y < y_limit:
                    if not visited[next_x][next_y] and image[next_x][next_y] == target:
                        image[next_x][next_y] = color
                        visited[next_x][next_y] = True
                        q.append((next_x, next_y))
        
        return image