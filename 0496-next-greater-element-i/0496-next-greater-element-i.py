class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        greater_nums = {}
        
        for num2 in nums2:
            while stack and num2 > stack[-1]:
                greater_nums[stack.pop()] = num2
            stack.append(num2)
        
        answer = []
        for num1 in nums1:
            answer.append(greater_nums.get(num1, -1))
        
        
        return answer