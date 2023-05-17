class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        sandwiches = deque(sandwiches)
        
        while students and sandwiches and sandwiches[0] in students:
            if students[0] == sandwiches[0]:
                students.popleft()
                sandwiches.popleft()
            else:
                students.append(students.popleft())
        
        return len(students)