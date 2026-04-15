class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = -1, 0
        for weight in weights:
            l = max(l, weight)
            r += weight
        while l < r:
            m = l + (r - l) // 2
            daysNeeded, curr = 1, 0
            for weight in weights:
                if curr + weight > m:
                    daysNeeded += 1
                    curr = 0
                curr += weight
            if daysNeeded > days:
                l = m + 1
            else:
                r = m
        return l