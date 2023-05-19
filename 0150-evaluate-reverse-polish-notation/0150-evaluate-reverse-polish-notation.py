class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                stack.append(stack.pop() + stack.pop())
            elif token == '-':
                last = stack.pop()
                llast = stack.pop()
                stack.append(llast - last)
            elif token == '*':
                stack.append(stack.pop() * stack.pop())
            elif token == '/':
                last = stack.pop()
                llast = stack.pop()
                stack.append(int(llast / last))
            else:
                stack.append(int(token))
                
        return stack[0]