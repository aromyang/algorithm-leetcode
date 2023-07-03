class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first = set('qwertyuiop')
        second = set('asdfghjkl')
        third = set('zxcvbnm')
        
        ans = []
        
        for word in words:
            unique = set(word.lower())
            if unique.issubset(first) or unique.issubset(second) or unique.issubset(third):
                ans.append(word)

        return ans