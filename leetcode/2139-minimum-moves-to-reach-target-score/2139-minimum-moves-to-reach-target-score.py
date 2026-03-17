class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:

        store = []
        t = target
        temp = maxDoubles
        side = 0
        while temp > 0 and t > 1:
            if t % 2 and t != 1:
                side += 1
            t //= 2
            store.append(t)
            temp -= 1
        if store: return len(store) + side + store[-1] - 1
        return target - 1
 