class Solution:
    def firstUniqChar(self, s: str) -> int:
        alphas = {}
        for i, ss in enumerate(s):
            if ss not in alphas:
                alphas[ss] = i
            else:
                alphas[ss] = -1
        
        valid_idxes = [idx for idx in alphas.values() if idx != -1]

        return -1 if not valid_idxes else min(valid_idxes)
