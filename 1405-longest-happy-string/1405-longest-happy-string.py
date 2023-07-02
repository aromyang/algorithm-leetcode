class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = []
        if a != 0:
            heappush(max_heap, (-a, 'a'))
        if b != 0:
            heappush(max_heap, (-b, 'b'))
        if c != 0:
            heappush(max_heap, (-c, 'c'))

        ans = ''

        while max_heap:
            count1, char1 = heappop(max_heap)
            if ans[-2:] == char1 * 2:
                if not max_heap:
                    break
                else:
                    count2, char2 = heappop(max_heap)
                    ans += char2
                    if count2 < -1:
                        heappush(max_heap, (count2 + 1, char2))
                    heappush(max_heap, (count1, char1))
            else:
                ans += char1
                if count1 < -1:
                    heappush(max_heap, (count1 + 1, char1))

        return ans
