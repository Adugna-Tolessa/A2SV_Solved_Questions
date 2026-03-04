class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return
        r, c = len(matrix), len(matrix[0])
        self.prefix = [[0] * (c + 1) for _ in range(r + 1)]
        for i in range(1, r + 1):
            for j in range(1, c + 1):
                self.prefix[i][j] = matrix[i-1][j-1] + self.prefix[i-1][j] + self.prefix[i][j-1] - self.prefix[i-1][j-1]
                

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1 += 1
        col1 += 1
        row2 += 1
        col2 += 1
        return self.prefix[row2][col2] - self.prefix[row1-1][col2] - self.prefix[row2][col1-1] + self.prefix[row1-1][col1-1]
        