class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        cnt = Counter(arr)
        sorted_cnts = sorted(list(cnt.values()))
        target = len(arr) // 2
        cur_num = 0
        ans = 0
        
        while cur_num < target:
            cur_num += sorted_cnts.pop()
            ans += 1
        
        return ans