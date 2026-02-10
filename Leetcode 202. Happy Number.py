class Solution:
    def isHappy(self, n: int) -> bool:
        t = str(n)
        store = defaultdict(int)
        ans = 0
        store[int(n)] += 1
        while int(t) > 1:

            for i in t:
                ans += (int(i) ** 2)
            t = str(ans)
            
            store[int(t)] += 1
            if store[ans] > 1:
                return False
            ans = 0
        return True


