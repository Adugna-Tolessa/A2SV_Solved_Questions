class Solution:
    def sumAndMultiply(self, n: int) -> int:
        num = str(n)
        x = ""
        tot = 0
        for i in range(len(num)):
            tot += int(num[i])
            if int(num[i]):
                x += num[i]
        x = int(x) if len(x) else 0
        x *= tot
        return x