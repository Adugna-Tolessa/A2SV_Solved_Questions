class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        self.dxns = [[1,0],[0,1],[-1,0],[0,-1]]
        def dfs(rw, col, h, seen):
            if (rw,col, h) in seen:
                return False
            seen.add((rw,col, h))
            if h == 0:
                return False
            nw_h = h
            if grid[rw][col] == 1:
                nw_h -= 1
            if rw == len(grid) - 1 and col == len(grid[0]) - 1:
                if nw_h > 0:
                    return True
                return False
            ans = False
            for dxn in self.dxns:
                nw_r = rw + dxn[0]
                nw_c = col + dxn[1]
                if nw_r < 0 or nw_r >= len(grid) or nw_c < 0 or nw_c >= len(grid[0]):
                    continue
                ans = ans or dfs(nw_r, nw_c, nw_h, seen)
            return ans
        return dfs(0,0, health, set())