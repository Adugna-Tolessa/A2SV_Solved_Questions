class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        store = defaultdict(lambda: 0)
        stack = []
        for i, n in enumerate(temperatures):
            while stack and stack[-1][1] < n:
                temp = stack.pop()
                store[temp[0]] = i
            stack.append([i, n])
        print(store)
        ans = []

        for i in range(len(temperatures)):
            if i in store:
                ans.append(store[i] - i)
            else:
                ans.append(0)
        return ans