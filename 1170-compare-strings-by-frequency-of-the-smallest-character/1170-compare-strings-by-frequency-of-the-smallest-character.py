class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        nums = {}
        ans = []
        
        for word in words:
            smallest_w = sorted(Counter(word).items())[0][1]
            nums[smallest_w] = nums.get(smallest_w, 0) + 1
                
        for query in queries:
            smallest_q = sorted(Counter(query).items())[0][1]
            ans.append(sum(v for k, v in nums.items() if k > smallest_q))
                
        return ans