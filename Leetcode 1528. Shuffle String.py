class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        store = defaultdict(int)
        i = 0
        for key in s:
            store[indices[i]] = key
            i += 1
        ans = []
        n = max(indices) + 1
        for idx in range(n):
            ans.append(store[idx])
        return "".join(ans)
