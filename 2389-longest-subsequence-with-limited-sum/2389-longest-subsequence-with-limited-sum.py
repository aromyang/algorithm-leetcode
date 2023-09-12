class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        n_sum = [0]
        
        for num in nums:
            n_sum.append(n_sum[-1] + num)
        n_sum = n_sum[1:]
            
        ans = []
        
        for query in queries:
            left, right = 0, len(nums) - 1
            
            while left <= right:
                mid = (left + right) // 2
                if n_sum[mid] > query:
                    right = mid - 1
                else:
                    left = mid + 1
                    
            ans.append(left)
        
        return ans