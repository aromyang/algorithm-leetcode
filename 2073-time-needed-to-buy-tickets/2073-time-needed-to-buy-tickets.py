class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque((i, tickets[i]) for i in range(len(tickets)))
        cnt = 0
        
        while queue:
            idx, left = queue.popleft()
            left -= 1
            cnt += 1
            
            if idx == k and left == 0:
                return cnt
            
            if left != 0:
                queue.append((idx, left))
                    
        return cnt