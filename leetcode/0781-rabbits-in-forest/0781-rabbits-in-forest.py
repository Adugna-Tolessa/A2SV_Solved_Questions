class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        cnt = Counter(answers)
        ans = 0
        print(cnt)
        for key in cnt:
            temp = ceil(cnt[key] / (key + 1))
            ans += (key + 1) * temp
        return ans