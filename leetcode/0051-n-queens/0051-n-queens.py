class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        up = set()
        down = set()
        board = [["."] * n for _ in range(n)]
        ans = []

        def backtrack(r):
            if r == n:
                temp = []
                for row in board:
                    temp.append("".join(row))
                ans.append(temp)
                return

            for c in range(n):
                if c in col or r - c in down or r + c in up:
                    continue
                col.add(c)
                up.add(r + c)
                down.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                col.remove(c)
                up.remove(r + c)
                down.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return ans