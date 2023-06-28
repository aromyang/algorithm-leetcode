class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest_heap = []

        for point in points:
            distance = point[0] ** 2 + point[1] ** 2
            if len(closest_heap) < k:
                heappush(closest_heap, (-distance, point))
            else:
                heappushpop(closest_heap, (-distance, point))
        
        return [heappop(closest_heap)[1] for _ in range(k)]