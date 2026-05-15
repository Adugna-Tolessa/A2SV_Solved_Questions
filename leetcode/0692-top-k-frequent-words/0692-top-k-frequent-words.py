class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = Counter(words)
        h = []
        for key in cnt:
            heappush(h, (-cnt[key], key))
        res = []
        for _ in range(k):
            temp, key = heappop(h)
            res.append(key)
        return res