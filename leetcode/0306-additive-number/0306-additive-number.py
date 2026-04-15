class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        def backtrack(i, j, k):
            a = int(num[0:i])
            b = int(num[i:j])
            while j < n:
                c = a + b
                c_str = str(c)
                if not num.startswith(c_str, j):
                    return False
                j += len(c_str)
                a, b = b, c
            return True

        for i in range(1, n):
            for j in range(i + 1, n):
                if (num[0] == "0" and i > 1) or (num[i] == "0" and j - i > 1):
                    continue
                if backtrack(i, j, j):
                    return True

        return False