class Solution:
    def splitString(self, s: str) -> bool:
        def backtrack(idx, parts, prev):
            if idx == len(s):
                return parts >= 2
            for i in range(idx, len(s)):
                num = int(s[idx: i + 1])
                if prev == -1 or num == prev - 1:
                    if backtrack(i + 1, parts + 1, num):
                        return True
            return False
        return backtrack(0,0,-1)
        