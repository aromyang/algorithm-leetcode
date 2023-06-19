class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        ones = [(Counter(m)[1], idx) for idx, m in enumerate(mat)]
        ones.sort(key=lambda x:(x[0], x[1]))
        
        return [one[1] for one in ones[:k]]