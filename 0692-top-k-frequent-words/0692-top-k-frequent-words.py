class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = Counter(words).most_common()
        cnt.sort(key=lambda x: (-x[1], x[0]))
        return [cnt[i][0] for i in range(k)]