# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        check = {}
        left = 0
        right = n
        
        while True:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid - 1
                check[mid] = True
                if mid-1 in check and not check[mid-1]:
                    return mid
            else:
                left = mid + 1
                check[mid] = False
                if mid+1 in check and check[mid+1]:
                    return mid+1
                