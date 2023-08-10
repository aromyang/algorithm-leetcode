class Solution:
    def longestWord(self, words: List[str]) -> str:
        ans = ''
        words = set(words)
        
        for word in words:
            if len(word) > len(ans) or (len(word) == len(ans) and word < ans):
                temp = ''
                for w in word:
                    temp += w
                    if temp not in words:
                        break
                else:
                    ans = temp
                    
        return ans