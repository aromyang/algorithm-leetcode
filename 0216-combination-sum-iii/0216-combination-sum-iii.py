class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(start, k, n, path, ans):
            if k == 0 and n == 0:
                ans.append(path)
                return
            if k == 0 or n < 0:
                return
            if n < (start + start + k - 1) * k // 2:
                return
            for i in range(start, 10):
                if n - i < 0:
                    break
                backtrack(i + 1, k - 1, n - i, path + [i], ans)
                
        
        ans = []
        backtrack(1, k, n, [], ans)
        
        return ans