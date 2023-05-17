class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        discount = {}
        
        for i in range(len(prices)):
            while stack and stack[-1][1] >= prices[i]:
                idx, _ = stack.pop()
                discount[idx] = prices[i]
            stack.append((i, prices[i]))
                    
        for j in range(len(prices)):
            if j in discount:
                prices[j] -= discount[j]
        
        return prices
                