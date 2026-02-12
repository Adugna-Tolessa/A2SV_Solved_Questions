class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        word1 = list(word1)
        word2 = list(word2)
        word1_count = Counter(word1)
        word2_count = Counter(word2)

        if len(word1) != len(word2):
            return False
            
        word1.sort(key = lambda a: -word1_count[a])
        word2.sort(key = lambda a: -word2_count[a])

        for i in range(len(word1)):
            if word1[i] not in word2_count.keys() or word2[i] not in word1_count.keys():
                return False
            elif word1_count[word1[i]] != word2_count[word2[i]]:
                return False
        return True
