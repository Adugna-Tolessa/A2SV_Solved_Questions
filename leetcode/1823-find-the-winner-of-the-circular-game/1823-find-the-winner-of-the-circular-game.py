class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def winner(n, k):
            if n == 1:
                return 0
            return (winner(n - 1, k) + k) % n
        return winner(n, k) + 1