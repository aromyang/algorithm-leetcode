class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        bans = set([b.lower() for b in banned])
        symbols = '!?\',;.'
        paragraph = re.sub('[!?\',;. ]', ' ', paragraph.lower()).split()
        words = Counter(paragraph).most_common()

        for word in words:
            if word[0] not in bans:
                return word[0]
        
        return ''