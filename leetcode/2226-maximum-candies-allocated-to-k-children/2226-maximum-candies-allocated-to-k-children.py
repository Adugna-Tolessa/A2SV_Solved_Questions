class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        l, r = 1, max(candies)
        ans = 0
        while l <= r:
            m = l + (r - l) // 2
            cnt = 0
            for pile in candies:
                cnt += (pile // m)
            if cnt >= k:
                ans = m
                l = m + 1
            else:
                r = m - 1
        return ans