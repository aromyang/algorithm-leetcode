class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        nums.sort()
        ans = nums[-1]
        
        left, right = 1, nums[-1]
        while left <= right:
            mid = (left + right) // 2
            cur = 0
            for num in nums:
                cur += math.ceil(num / mid)
                if cur > threshold:
                    left = mid + 1
                    break
            else:
                if cur <= threshold:
                    ans = min(mid, ans)
                    right = mid - 1
                else:
                    left = mid + 1
                    
        return ans