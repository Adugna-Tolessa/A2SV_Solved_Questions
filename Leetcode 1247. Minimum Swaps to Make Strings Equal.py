class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        s1_count = Counter(s1)
        s2_count = Counter(s2)
        xy, yx = 0, 0
        for i in range(len(s1)):
            if s1[i] != s2[i] and s1[i] == "x":
                xy += 1
            elif s1[i] != s2[i] and s1[i] == "y":
                yx += 1
        if (xy + yx) % 2:
            return -1
        ans = xy // 2
        ans += yx // 2
        if xy % 2 == 1:
            ans += 2
        
        return ans

