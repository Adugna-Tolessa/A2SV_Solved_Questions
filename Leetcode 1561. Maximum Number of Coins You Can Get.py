class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = True)
        ans = 0
        n = len(piles) // 3

        for i in range(1, len(piles) - n, 2):
            ans += piles[i]
            
        return ans
