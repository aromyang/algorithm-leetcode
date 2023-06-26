class SmallestInfiniteSet:

    def __init__(self):
        self.removed_set = set()
        self.min_num = 1

    def popSmallest(self) -> int:
        if self.removed_set:
            while self.min_num in self.removed_set:
                self.min_num += 1
        self.removed_set.add(self.min_num)
        return self.min_num
            
    def addBack(self, num: int) -> None:
        if num in self.removed_set:
            self.removed_set.remove(num)
        self.min_num = min(self.min_num, num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)