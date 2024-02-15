class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        connection_dict = defaultdict(set)
        
        for from_, to in roads:
            connection_dict[from_].add(to)
            connection_dict[to].add(from_)

        ans = 0
            
        for i in range(n):
            for j in range(i + 1, n):
                cur = len(connection_dict[i]) + len(connection_dict[j])
                if j in connection_dict[i]:
                    cur -= 1
                ans = max(ans, cur)
        
        return ans