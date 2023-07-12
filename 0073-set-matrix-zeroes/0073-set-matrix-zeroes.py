class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        visited = set()
        for i, row in enumerate(matrix):
            for j, cell in enumerate(row):
                if cell == 0 and (i, j) not in visited:
                    for cur_j, cur_cell in enumerate(matrix[i]):
                        if matrix[i][cur_j] != 0:
                            matrix[i][cur_j] = 0
                            visited.add((i, cur_j))
                    for col in range(len(matrix)):
                        if matrix[col][j] != 0:
                            matrix[col][j] = 0
                            visited.add((col, j))