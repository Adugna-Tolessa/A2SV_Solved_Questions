class Solution:
    def frequencySort(self, s: str) -> str:
        store = Counter(s)
        print(store)
        s = list(s)
        s.sort(key = lambda a: [-store[a], a])
        return "".join(s)
