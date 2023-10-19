class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        x_limit, y_limit = len(board), len(board[0])
        ans = 0
        
        for x in range(x_limit):
            for y in range(y_limit):
                if board[x][y] == '.':
                    continue
                if x > 0 and board[x-1][y] == 'X':
                    continue
                if y > 0 and board[x][y-1] == 'X':
                    continue
                ans += 1
        
        return ans