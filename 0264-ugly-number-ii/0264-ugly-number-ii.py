class Solution:
    def nthUglyNumber(self, n: int) -> int:
        min_heap = [1]
        dup = set()
        ans = []
        
        while len(ans) < n:
            cur_num = heappop(min_heap)
            if cur_num not in dup:
                dup.add(cur_num)
                ans.append(cur_num)
                heappush(min_heap, cur_num * 2)
                heappush(min_heap, cur_num * 3)
                heappush(min_heap, cur_num * 5)
        
        ans.sort()
        return ans[n - 1]