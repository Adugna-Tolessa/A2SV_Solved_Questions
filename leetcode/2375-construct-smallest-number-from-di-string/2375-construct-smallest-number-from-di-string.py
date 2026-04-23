class Solution:
    def smallestNumber(self, pattern: str) -> str:
        used = [0] * 10
        ans = []
        def backtrack(arr):
            if len(arr) == len(pattern) + 1:
                ans.append("".join(map(str, arr)))
                return True
            for n in range(1, 10):
                if used[n]:
                    continue
                if arr:
                    i = len(arr) - 1
                    if pattern[i] == 'I' and arr[-1] >= n:
                        continue
                    if pattern[i] == 'D' and arr[-1] <= n:
                        continue

                used[n] = 1
                arr.append(n)

                if backtrack(arr):
                    return True

                arr.pop()
                used[n] = 0

            return False
        backtrack([])
        return ans[0]