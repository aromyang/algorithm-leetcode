class Solution:

    def __init__(self, nums: List[int]):
        self.dict = defaultdict(list)
        for i, num in enumerate(nums):
            self.dict[num].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.dict[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)