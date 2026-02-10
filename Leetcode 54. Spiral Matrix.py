class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        a, b, c, d = [0, 0], [0, len(matrix[0]) - 1], [len(matrix) - 1, len(matrix[0]) - 1], [len(matrix) - 1, 0]
        i, j = 0, 0
        temp = len(matrix) * len(matrix[0])

        while temp:
            while j <= b[1] and temp > 0:
                ans.append(matrix[i][j])
                temp -= 1
                j += 1
            j -= 1
            i += 1
            a[0] += 1

            while i <= c[0] and temp > 0:
                ans.append(matrix[i][j])
                temp -= 1
                i += 1
            i -= 1
            j -= 1
            b[1] -= 1

            while j >= d[1] and temp > 0:
                ans.append(matrix[i][j])
                temp -= 1
                j -= 1
            j += 1
            i -= 1
            c[0] -= 1

            while i >= a[0] and temp > 0:
                ans.append(matrix[i][j])
                temp -= 1
                i -= 1
            i += 1
            j += 1
            d[1] += 1

        return ans
