class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return True if word.islower() or word.istitle() or word.isupper() else False