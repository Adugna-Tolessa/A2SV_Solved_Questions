class Solution:
    def solveSudoku(self, board):
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    val = board[r][c]
                    rows[r].add(val)
                    cols[c].add(val)
                    squares[(r//3, c//3)].add(val)

        def backtrack(r, c):
            if r == 9:
                return True
            if c == 9:
                return backtrack(r + 1, 0)
            if board[r][c] != ".":
                return backtrack(r, c + 1)

            for val in "123456789":
                if val not in rows[r] and val not in cols[c] and val not in squares[(r // 3, c // 3)]:
                    board[r][c] = val
                    rows[r].add(val)
                    cols[c].add(val)
                    squares[(r//3, c//3)].add(val)

                    if backtrack(r, c + 1):
                        return True

                    board[r][c] = "."
                    rows[r].remove(val)
                    cols[c].remove(val)
                    squares[(r//3, c//3)].remove(val)

            return False

        backtrack(0, 0)