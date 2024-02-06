class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        dict_ = {idx: connections for idx, connections in enumerate(graph)}
        ans = []
        
        def dfs(path, connections):
            if not connections:
                return
            
            for connection in connections:
                if connection == target:
                    ans.append(path + [connection])
                else:
                    dfs(path + [connection], dict_[connection])
                
        
        for connection in dict_[0]:
            if connection == target:
                ans.append([0, connection])
            else:
                dfs([0, connection], dict_[connection])
                
        return ans
                