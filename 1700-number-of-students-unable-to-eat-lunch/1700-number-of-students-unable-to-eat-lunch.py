class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        answer = 0
        students = deque(students)
        sandwiches = deque(sandwiches)
        
        while sandwiches:
            current = sandwiches.popleft()
            if current not in students:
                break
                
            while students:
                if current == students[0]:
                    students.popleft()
                    break
                else:
                    students.append(students.popleft())
        
        return len(students)