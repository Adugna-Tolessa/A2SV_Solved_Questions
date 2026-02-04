class Solution:
    def checkEqual(self, a, b) -> bool:
        A = sorted(a)
        B = sorted(b)
        if A == B and len(a) == len(b):
            return True
        else: return False
