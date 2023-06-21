class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-gift for gift in gifts]
        heapify(gifts)
        
        while k > 0:
            k -= 1
            mmax = -heappop(gifts)
            heappush(gifts, -int(math.sqrt(mmax)))
        
        return -sum(list(gifts))