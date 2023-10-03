class MyCalendar:

    def __init__(self):
        self.cal = []

    def book(self, start: int, end: int) -> bool:
        end -= 1        
        for c_start, c_end in self.cal:
            left, right = start, end
            while left <= right:
                mid = (left + right) // 2
                if c_start <= mid <= c_end:
                    return False
                elif mid <= c_start:
                    left = mid + 1
                else:
                    right = mid - 1
        
        self.cal.append([start, end])
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)