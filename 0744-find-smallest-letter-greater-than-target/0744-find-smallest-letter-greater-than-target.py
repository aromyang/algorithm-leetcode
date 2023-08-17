class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters) - 1
        
        while left <= right:
            mid = (left + right) // 2
            cur = letters[mid]
            
            if cur <= target:
                left = mid + 1
            elif cur > target:
                right = mid - 1
                
        return letters[left] if left < len(letters) else letters[0]