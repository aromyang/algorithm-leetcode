class Solution:
    def isHappy(self, n: int) -> bool:
        done = set()
        num = 0
        while num != 1:
            num = 0
            for i in range(len(str(n))):
                num += int(str(n)[i]) ** 2
            if num in done:
                return False
            done.add(num)
            n = num
        return True