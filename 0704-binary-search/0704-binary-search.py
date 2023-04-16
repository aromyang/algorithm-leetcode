class Solution:
    def search(self, nums: List[int], target: int) -> int:      
        left = 0
        right = len(nums) - 1
                
        while True:
            if nums[left] > target or nums[right] < target:
                return -1
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else: 
                left = mid + 1