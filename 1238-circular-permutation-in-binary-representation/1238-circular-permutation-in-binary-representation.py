class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        gray_codes = [i ^ (i >>1) for i in range(2 ** n)]
        start_idx = gray_codes.index(start)
        return gray_codes[start_idx:] + gray_codes[:start_idx]