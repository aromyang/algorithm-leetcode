class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cur_idx = 0
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[cur_idx] = nums[i]
                cur_idx += 1
        
        return cur_idx