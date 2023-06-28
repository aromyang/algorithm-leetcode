class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        flat = [m for inner in matrix for m in inner]
        flat.sort()
        
        return flat[k - 1]