class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closet_heap = []
        for point in points:
            distance = math.sqrt(point[0] ** 2 + point[1] ** 2)
            heappush(closet_heap, (distance, point))
        
        return [heappop(closet_heap)[1] for _ in range(k)]