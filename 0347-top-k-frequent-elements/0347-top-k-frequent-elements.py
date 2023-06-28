class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnts = Counter(nums)
        frequents = sorted(list(zip(cnts.values(), cnts.keys())), key = lambda x : x[0], reverse=True)
        
        return [x[1] for x in frequents[:k]]