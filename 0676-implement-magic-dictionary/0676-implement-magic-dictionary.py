class MagicDictionary:

    def __init__(self):
        self.dict = set()

    def buildDict(self, dictionary: List[str]) -> None:
        for d in dictionary:
            self.dict.add(d)

    def search(self, searchWord: str) -> bool:
        for d in self.dict:
            if len(d) == len(searchWord):
                if sum(1 for c1, c2 in zip(d, searchWord) if c1 != c2) == 1:
                    return True
        return False
        
        
# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)