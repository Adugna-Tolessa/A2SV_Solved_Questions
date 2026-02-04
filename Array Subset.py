from collections import Counter
class Solution:
    def isSubset(self, a, b):
        x = Counter(a)
        y = Counter(b)
        for i in y:
            if y[i] > x[i]:
                return False
        return True
