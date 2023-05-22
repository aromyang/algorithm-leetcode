class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        stack = []
        cur_num = 0 
        operator = '+'

        for i in range(len(s)):
            if s[i].isdigit():
                cur_num = cur_num * 10 + int(s[i])
            if not s[i].isdigit() or i == len(s) - 1:
                if operator == '+':
                    stack.append(cur_num)
                elif operator == '-':
                    stack.append(-cur_num)
                elif operator == '*':
                    stack.append(stack.pop() * cur_num)
                elif operator == '/':
                    stack.append(int(stack.pop() / cur_num))
                
                operator = s[i]
                cur_num = 0
                
        return sum(stack)
