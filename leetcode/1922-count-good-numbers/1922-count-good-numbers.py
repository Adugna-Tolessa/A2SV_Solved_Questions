class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10 ** 9 + 7
        # ans = 1
        # for i in range(n):
        #     if i % 2 == 0:
        #         ans *= 5
        #     else:
        #         ans *= 4
        # return ans % (10 ** 9 + 7)
        def res(par, num):
            a = 1
            b = par
            while num > 0:
                if num % 2 == 1:
                    a = a * b % mod
                b = b * b % mod
                num //= 2
            return a

        return res(5, (n + 1) // 2) * res(4, n // 2) % mod