class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        types = Counter(candyType)
        
        return min(len(types), len(candyType) // 2)