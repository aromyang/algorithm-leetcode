class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word == word.upper() or word == word.lower():
            return True
        elif word[:1] == word[:1].upper() and word[1:] == word[1:].lower():
            return True
        else:
            return False