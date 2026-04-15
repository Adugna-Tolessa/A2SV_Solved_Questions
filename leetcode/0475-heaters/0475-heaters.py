class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        rad = 0
        for house in houses:
            l, r = 0, len(heaters) - 1
            while l < r:
                m = l + (r - l) // 2
                if heaters[m] < house:
                    l = m + 1
                else:
                    r = m
            dist = abs(heaters[l] - house)
            if l > 0:
                dist = min(dist, abs(heaters[l - 1] - house))
            rad = max(rad, dist)
        return rad