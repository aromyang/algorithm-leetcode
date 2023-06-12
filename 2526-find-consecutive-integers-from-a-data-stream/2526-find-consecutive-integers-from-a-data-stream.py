class DataStream:

    def __init__(self, value: int, k: int):
        self.stream = deque([])
        self.k = k
        self.value = value

    def consec(self, num: int) -> bool:
        if len(self.stream) >= self.k:
            self.stream.popleft()
        self.stream.append(num == self.value)
                
        return all(self.stream) if len(self.stream) >= self.k else False
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)