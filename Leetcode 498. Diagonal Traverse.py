class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        i, j = 0, 0
        rows, cols = len(mat), len(mat[0])
        ans = []

        while len(ans) < rows * cols:
            while i >= 0 and j < cols:
                ans.append(mat[i][j])
                i -= 1
                j += 1

            i += 1
            if j >= cols:
                j -= 1
                i += 1

            while i < rows and j >= 0:
                ans.append(mat[i][j])
                j -= 1
                i += 1

            j += 1
            if i >= rows:
                i -= 1
                j += 1
        
        return ans
