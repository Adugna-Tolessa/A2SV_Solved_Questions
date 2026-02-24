class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        store = defaultdict(int)
        for c, key in enumerate(s):
            store[key] = c
        ans = []
        r = 0
        l = 0
        for i, char in enumerate(s):
            r = max(r, store[char])
            if i == r:
                ans.append(r - l + 1)
                l = i + 1
        return ans
