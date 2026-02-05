from collections import Counter
class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        ans = 0
        master_map = Counter(chars)
        
        for word in words:
            word_map = Counter(word)
            for char, count in word_map.items():
                if count > master_map[char]:
                    break
            else:
                ans += len(word)
        return ans
