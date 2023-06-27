class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = Counter(s)
        cnt_list = list(zip(cnt.keys(), cnt.values()))
        cnt_list.sort(key=lambda x : x[1], reverse=True)
        cnt_list = [x[0] * x[1] for x in cnt_list]
    
        return "".join(cnt_list)