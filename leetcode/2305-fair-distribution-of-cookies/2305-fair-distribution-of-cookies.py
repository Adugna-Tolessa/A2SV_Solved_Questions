class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        arr = [0] * k
        self.ans = float("inf")
        def backtrack(idx):
            if idx == len(cookies):
                self.ans = min(self.ans, max(arr))
                return
            for i in range(k):
                arr[i] += cookies[idx]
                if arr[i] < self.ans:
                    backtrack(idx + 1)
                arr[i] -= cookies[idx]
                if arr[i] == 0:
                    break
        backtrack(0)
        return self.ans