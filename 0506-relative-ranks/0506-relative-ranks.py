class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ranks = sorted(score, reverse=True)
        answer = []
        
        for s in score:
            rank = ranks.index(s) + 1
            if rank == 1:
                rank = "Gold Medal"
            elif rank == 2:
                rank = "Silver Medal"
            elif rank == 3:
                rank = "Bronze Medal"
                
            answer.append(str(rank))
            
        return answer