class MyCalendar:

    def __init__(self):
        self.cal = []

    def book(self, start: int, end: int) -> bool:
        idx_start = bisect.bisect_right(self.cal, start)
        
        if idx_start & 1:
            return False
        
        idx_end = bisect.bisect_left(self.cal, end)
        if idx_end != idx_start:
            return False
        
        bisect.insort(self.cal, start)
        bisect.insort(self.cal, end)
        
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)