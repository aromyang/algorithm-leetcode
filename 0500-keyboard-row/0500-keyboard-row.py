class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first = set(['q','w','e','r','t','y','u','i','o','p'])
        second = set(['a','s','d','f','g','h','j','k','l'])
        third = set(['z','x','c','v','b','n','m'])
        
        ans = []
        
        for word in words:
            unique = set(word.lower())
            if unique.issubset(first) or unique.issubset(second) or unique.issubset(third):
                ans.append(word)

        return ans