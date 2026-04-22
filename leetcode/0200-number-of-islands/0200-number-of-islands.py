class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rws = len(grid)
        cols = len(grid[0])
        dxn = [(1,0), (-1, 0), (0, 1), (0, -1)]
        cnt = 0
        def dfs(r, c):
            if r < 0 or r == rws or c < 0 or c == cols or grid[r][c] == "0":
                return
            grid[r][c] = "0"
            for i in range(4):
                dfs(r + dxn[i][0], c + dxn[i][1])
        for i in range(rws):
            for j in range(cols):
                if grid[i][j] == "1":
                    cnt += 1
                    dfs(i, j) 
        return cnt