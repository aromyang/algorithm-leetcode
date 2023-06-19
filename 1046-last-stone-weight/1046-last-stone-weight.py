class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heappush(heap, (-stone, stone))
        
        print(heap)
        
        while len(heap) > 1:
            print(heap)
            one = heappop(heap)[1]
            two = heappop(heap)[1]
            if one != two:
                result = one - two
                heappush(heap, (-result, result))
        
        return heappop(heap)[1] if heap else 0