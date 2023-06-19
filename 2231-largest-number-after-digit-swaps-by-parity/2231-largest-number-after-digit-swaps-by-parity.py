class Solution:
    def largestInteger(self, num: int) -> int:
        odd = []
        even = []
        nums = deque()
        while num > 0:
            number = num % 10
            nums.insert(0, number)
            if number & 1:
                heappush(odd, -number)
            else:
                heappush(even, -number)
            num //= 10
        
        answer = ''
        while nums:
            if nums.popleft() & 1:
                answer += str(-heappop(odd))
            else:
                answer += str(-heappop(even))
        
        return int(answer)