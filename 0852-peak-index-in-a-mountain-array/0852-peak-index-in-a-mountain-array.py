class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 1, len(arr) - 2
        
        while left <= right:
            mid = (left + right) // 2
            if arr[mid - 1] < arr[mid] and arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid - 1] < arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid - 1