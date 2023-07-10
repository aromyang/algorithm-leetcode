class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i, row in enumerate(board):
            row_distinct = set(row)
            row_numbers = ''.join(row).replace('.', '')
            
            if len(row_distinct) - 1 != len(row_numbers):
                return False
            
            col = [col[i] for col in board]
            col_distinct = set(col)
            col_numbers = ''.join(col).replace('.', '')
            
            if len(col_distinct) - 1 != len(col_numbers):
                return False
            
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
                box_distinct = set(box)
                box_numbers = ''.join(box).replace('.', '')
                
                if len(box_distinct) - 1 != len(box_numbers):
                    return False
            
        return True