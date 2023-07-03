class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cnt1 = Counter(nums1)
        cnt2 = Counter(nums2)
        ans = []
        
        for cnt in cnt1:
            if cnt in cnt2:
                ans.append(cnt)
                    
        return ans