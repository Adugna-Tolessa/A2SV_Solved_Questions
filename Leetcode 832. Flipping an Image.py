class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        row, col = len(image), len(image[0])

        matrix = []
        for m in image:
            matrix.append(m[::-1])
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 1:
                    matrix[r][c] = 0
                else:
                    matrix[r][c] = 1  
        return matrix
