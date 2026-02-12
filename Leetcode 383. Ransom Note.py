# from collections import Counter
# import collections

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r_count = Counter(ransomNote)
        m_count = Counter(magazine)
        for key in r_count:
            if r_count[key] > m_count[key]:
                return False
        return True
