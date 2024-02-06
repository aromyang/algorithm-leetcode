class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        linked_nodes = set()
        
        for from_, to_ in edges:
            linked_nodes.add(to_)
        
        return [node for node in range(n) if node not in linked_nodes]