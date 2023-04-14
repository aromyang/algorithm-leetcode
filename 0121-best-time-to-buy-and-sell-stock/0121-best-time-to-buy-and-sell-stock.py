class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = prices[0]
        for i in range(1, len(prices)):
            if min_price > prices[i]:
                min_price = prices[i]
            else:
                profit = max(profit, prices[i]-min_price)
        return profit