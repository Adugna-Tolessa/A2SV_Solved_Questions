class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        n, m = len(img), len(img[0])
        ans = [[0] * m for _ in range(n)]

        for row in range(n):
            for col in range(m):
                count = 0
                total = 0
                for r in range(row - 1, row + 2):
                    for c in range(col - 1, col + 2):
                        if r < 0 or r == n or c < 0 or c == m:
                            continue
                        total += img[r][c]
                        count += 1
                ans[row][col] = total // count
        return ans
                        
