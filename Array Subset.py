class Solution:
    def isSubset(self, a, b):
        # for i in range(len(b)):
        #     if b[i] not in a or len(b) > len(a):
        #         return False
        # return True
        # # return b.issubset(a)
    
    
        m, n = len(a), len(b)
        for i in range(n):
            found = False
            for j in range(m):
                if b[i] == a[j]:
                    found = True
                    a[j] = -1
                    break
            if not found:
                return False
        return True
