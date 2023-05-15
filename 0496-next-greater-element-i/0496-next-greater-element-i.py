class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = []
        
        for num1 in nums1:
            answer.append(-1)
            idx = nums2.index(num1)
            
            for j in range(idx, len(nums2)):
                if nums2[j] > num1:
                    answer.pop()
                    answer.append(nums2[j])
                    break
        
        return answer