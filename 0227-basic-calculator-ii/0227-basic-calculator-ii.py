class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        expressions = deque()
        
        for ss in s:
            if ss.isdigit():
                if expressions and expressions[-1].isdigit():
                    expressions.append(expressions.pop() + ss)
                else:
                    expressions.append(ss)
            elif ss != '':
                expressions.append(ss)
        
        
        deq = deque()
        
        while expressions:
            cur = expressions.popleft()
            if cur == '*':
                deq.append(int(deq.pop()) * int(expressions.popleft()))
            elif cur == '/':
                deq.append(int(deq.pop()) // int(expressions.popleft()))
            else:
                deq.append(cur)
        
        
        answer = int(deq.popleft())
        
        while deq:
            cur = deq.popleft()
            if cur == '+':
                answer += int(deq.popleft())
            elif cur == '-':
                answer -= int(deq.popleft())
            
        return answer