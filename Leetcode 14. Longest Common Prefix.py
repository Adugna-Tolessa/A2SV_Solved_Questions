class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = min(strs)
        n = len(s)
        temp = n
        if len(strs) == 1: return strs[0]
        for i in strs:
            for j in range(n):
                if i[j] == s[j]:
                    continue
                else:
                    temp = j
                    break
            n = temp
        return s[:n]
