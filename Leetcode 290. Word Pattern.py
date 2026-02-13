class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        arr = s.split()
        
        if len(arr) != len(pattern):
            return False
        p_to_w = {}
        w_to_p = {}
        for p, w in zip(pattern, arr):
            if p in p_to_w:
                if p_to_w[p] != w:
                    return False
            else:
                p_to_w[p] = w
            
            if w in w_to_p:
                if w_to_p[w] != p:
                    return False
            else:
                w_to_p[w] = p
        
        return True
