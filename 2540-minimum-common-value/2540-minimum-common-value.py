class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        small = nums1 if len(nums1) < len(nums2) else nums2
        big = nums2 if small is nums1 else nums1
        
        for s in small:
            left, right = 0, len(big) - 1
            while left <= right:
                mid = (left + right) // 2
                if big[mid] == s:
                    return s
                elif big[mid] > s:
                    right = mid - 1
                else:
                    left = mid + 1
        
        return -1