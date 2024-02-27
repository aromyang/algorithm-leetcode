class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        length = len(groups)
        
        ans = [words[0]]
        prev_group = groups[0]

        for i in range(1, length):
            cur_group = groups[i]
            if cur_group != prev_group:
                ans.append(words[i])
                prev_group = cur_group

        return ans