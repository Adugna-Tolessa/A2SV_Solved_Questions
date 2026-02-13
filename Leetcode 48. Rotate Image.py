class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        temp = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == j:
                    temp.append(j)
                elif j > temp[-1]:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for row in matrix:
            row.reverse()
