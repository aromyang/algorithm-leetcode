class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        max_heap = []
        min_heap = []
        answer = [0] * k
        
        for idx, num in enumerate(nums):
            heappush(max_heap, (-num, idx))
                    
        while len(min_heap) != k:
            heappush(min_heap, heappop(max_heap)[1])
                
        for i in range(k):
            answer[i] = nums[heappop(min_heap)]
            
        return answer