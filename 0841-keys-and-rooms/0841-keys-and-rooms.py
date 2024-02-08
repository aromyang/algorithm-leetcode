class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = set()

        def dfs(cur_v):
            if cur_v in seen:
                return
            
            seen.add(cur_v)
            
            for next_v in rooms[cur_v]:
                dfs(next_v)
                

        dfs(0)
               
        return len(seen) == len(rooms)