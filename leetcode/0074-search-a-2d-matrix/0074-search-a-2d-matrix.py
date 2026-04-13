class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rw, c = len(matrix), len(matrix[0])
        top, bottom = 0, rw - 1
        while top <= bottom:
            row = top + (bottom - top) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break
        else:
            return False
        row = top + (bottom - top) // 2 
        l, r = 0, c - 1
        while l<=r:
            m = l + (r - l) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False