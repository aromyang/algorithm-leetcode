class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        origin_con = defaultdict(set)
        both_con = defaultdict(set)
        
        for from_, to in connections:
            origin_con[from_].add(to)
            both_con[from_].add(to)
            both_con[to].add(from_)
        
        visited = set()
        self.ans = 0
        
        def dfs(cur):
            if cur in visited:
                return
            
            visited.add(cur)
            
            for to in both_con[cur]:
                if to not in visited:
                    if to in origin_con[cur]:
                        self.ans += 1
                    dfs(to)
        
        dfs(0)
        
        return self.ans
            