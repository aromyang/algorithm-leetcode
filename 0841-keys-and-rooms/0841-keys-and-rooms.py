class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = {}

        def dfs(cur_v):
            visited[cur_v] = True
            for next_v in rooms[cur_v]:
                if next_v not in visited:
                    dfs(next_v)

        dfs(0)
               
        return len(visited) == len(rooms)