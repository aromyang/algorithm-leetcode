class Solution:
    def fib(self, n: int) -> int:
        self.memo = {}
        
        def fibo(n):        
            if n <= 1:
                return n
            
            if n not in self.memo:
                self.memo[n] = fibo(n-1) + fibo(n-2)
            
            return self.memo[n]
            
        return fibo(n)