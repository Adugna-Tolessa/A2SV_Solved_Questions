class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxi = 0
        l, r = 0, len(height) - 1
        while l < r:
            if height[l] < height[r]:
                maxi = max(maxi, height[l] * (r - l))
                l += 1
            else:
                maxi = max(maxi, height[r] * (r - l))
                r -= 1
        return maxi
