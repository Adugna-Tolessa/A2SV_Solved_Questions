class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for word in strs:
            temp = [0] * 26
            for c in word:
                temp[ord(c) - ord("a")] += 1
            ans[tuple(temp)].append(word)
        return list(ans.values())
