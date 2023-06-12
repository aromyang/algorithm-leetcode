class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_deque = deque()
        max_deque = deque()
        left = 0
        answer = 0

        for right, num in enumerate(nums):
            while min_deque and num < min_deque[-1]:
                min_deque.pop()
            while max_deque and num > max_deque[-1]:
                max_deque.pop()

            min_deque.append(num)
            max_deque.append(num)

            if max_deque[0] - min_deque[0] > limit:
                if max_deque[0] == nums[left]:
                    max_deque.popleft()
                if min_deque[0] == nums[left]:
                    min_deque.popleft()
                left += 1

            answer = max(answer, right - left + 1)

        return answer
