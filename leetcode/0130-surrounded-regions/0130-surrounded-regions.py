class Solution:
    def solve(self, board: List[List[str]]) -> None:
        dxn = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rws, cols = len(board), len(board[0])
        def dfs(r, c):
            if r < 0 or c < 0 or r == rws or c == cols or board[r][c] != "O":
                return
            board[r][c] = "T"
            for i in range(4):
                dfs(r + dxn[i][0], c + dxn[i][1])
        for r in range(rws):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][cols - 1] == "O":
                dfs(r, cols - 1)
        for c in range(cols):
            if board[0][c] == "O":
                dfs(0, c)
            if board[rws - 1][c] == "O":
                dfs(rws - 1, c)
        for r in range(rws):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
    