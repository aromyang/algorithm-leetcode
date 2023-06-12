class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.q = deque([])

    def enQueue(self, value: int) -> bool:
        if len(self.q) >= self.k:
            return False
        else:
            self.q.append(value)
            return True

    def deQueue(self) -> bool:
        if not self.q:
            return False
        else:
            self.q.popleft()
            return True

    def Front(self) -> int:
        return -1 if not self.q else self.q[0]

    def Rear(self) -> int:
        return -1 if not self.q else self.q[-1]

    def isEmpty(self) -> bool:
        return not self.q

    def isFull(self) -> bool:
        return len(self.q) == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()