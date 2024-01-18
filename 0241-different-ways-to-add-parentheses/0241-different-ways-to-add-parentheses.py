class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        memo = {}
        
        def compute(left, right, op):
            results = []
            
            for l in left:
                for r in right:
                    if op == '+':
                        results.append(l + r)
                    elif op == '-':
                        results.append(l - r)
                    elif op == '*':
                        results.append(l * r)
                        
            return results
                
        
        def ways(expression):
            if expression in memo:
                return memo[expression]
            if expression.isdigit():
                return [int(expression)]
            
            ans = []
            
            for i, char in enumerate(expression):
                if char in "-+*":
                    left = ways(expression[:i])
                    right = ways(expression[i+1:])
                    
                    ans.extend(compute(left, right, char))
                    
            memo[expression] = ans
            return ans
            
        return ways(expression)