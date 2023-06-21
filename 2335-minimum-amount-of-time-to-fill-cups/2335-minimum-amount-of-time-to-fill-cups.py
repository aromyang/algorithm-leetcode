class Solution:
    def fillCups(self, amount: List[int]) -> int:
        amount = [a for a in amount if a != 0]
        seconds = 0
        
        while amount:
            if len(amount) == 1:
                seconds += amount.pop()
                break
            
            amount.sort()
            mmin = amount.pop(0)
            mmax = amount.pop()
            seconds += 1
            
            if mmin != 1:
                amount.append(mmin - 1)
            if mmax != 1:
                amount.append(mmax - 1)
            
        return seconds