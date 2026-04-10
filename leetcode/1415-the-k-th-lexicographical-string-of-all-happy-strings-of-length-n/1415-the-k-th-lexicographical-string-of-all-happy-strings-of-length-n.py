class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        store = []
        letters = ["a", "b", "c"]
        def backtrack(s, idx):
            if len(s) == n:
                store.append("".join(s))
                return
            for i in range(3):
                if s and s[-1] == letters[i]:
                    continue
                s.append(letters[i])
                backtrack(s, i + 1)
                s.pop()
        # return store[k - 1]
        backtrack([], 0)
        if k <= len(store): return store[k-1]
        return ""