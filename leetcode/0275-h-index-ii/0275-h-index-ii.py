class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l, r = 0, len(citations) - 1
        n = len(citations)
        while l <= r:
            m = l + (r - l) // 2
            if citations[m] < (n - m):
                l = m + 1
            elif citations[m] > (n - m):
                r = m - 1
            else:
                return citations[m]
        return n - l