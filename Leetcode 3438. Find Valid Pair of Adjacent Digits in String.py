class Solution:
    def findValidPair(self, s: str) -> str:
        store = Counter(s)
        print(store)
        for i in range(1, len(s)):
            if str(store[s[i]]) == s[i] and str(store[s[i - 1]]) == s[i - 1] and s[i] != s[i - 1]:
                return s[i - 1] + s[i]
        return ""
