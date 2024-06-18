class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.characters = characters
        self.combination_len = combinationLength
        self.cur_idx = 0
        self.combinations = []
        self._create_combinations(0, [])
        
    def _create_combinations(self, start: int, cur_combination: list):
        if len(cur_combination) == self.combination_len:
            self.combinations.append(''.join(cur_combination))
            return
        for i in range(start, len(self.characters)):
            cur_combination.append(self.characters[i])
            self._create_combinations(i + 1, cur_combination)
            cur_combination.pop()

    def next(self) -> str:
        result = self.combinations[self.cur_idx]
        self.cur_idx += 1
        return result

    def hasNext(self) -> bool:
        return self.cur_idx < len(self.combinations)


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()