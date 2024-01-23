class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        kth = {1: "0"}
        
        def invert(x):
            return ''.join('1' if bit == '0' else '0' for bit in x)
        def reverse(x):
            return x[::-1]
        
        def find_bit(n):
            if n not in kth:
                prev = find_bit(n-1)
                kth[n] = prev + "1" + reverse(invert(prev))
                
            return kth[n]
                        
        return find_bit(n)[k-1]