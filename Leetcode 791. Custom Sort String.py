class Solution:
    def customSortString(self, order: str, s: str) -> str:
        res = list(s)
        # temp = list(order)
        store = Counter(s)
        ans = ""
        t = []
        not_needed = []
        for i in range(len(s)):
            if s[i] not in order:
                t.append(s[i])
                del store[s[i]]
        for j in range(len(order)):
            if order[j] in store.keys():
                res = "".join([order[j]] * store[order[j]])
                ans += res
                # del store[order[j]]
        temp = "".join(t)
        return ans + temp

        # res.sort(key = lambda x: (x in temp))
