class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums = [num for num in nums if num != 0]
        heapify(nums)
        cnt = 0
        
        while nums:
            now = heappop(nums)
            nums = [num - now for num in list(nums) if num - now != 0]
            heapify(nums)
            cnt += 1
        
        return cnt