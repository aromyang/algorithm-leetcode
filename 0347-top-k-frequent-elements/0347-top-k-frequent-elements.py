class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnts = Counter(nums)
        cnts = [(-value, key) for key, value in cnts.items()]
        heapify(cnts)
        
        answer = []
        
        for i in range(k):
            _, ans = heappop(cnts)
            answer.append(ans)
        
        return answer