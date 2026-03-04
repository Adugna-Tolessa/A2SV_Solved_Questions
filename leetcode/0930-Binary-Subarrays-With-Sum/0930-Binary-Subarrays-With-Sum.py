class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        res = 0
        curSum = 0
        pref = defaultdict(int)
        pref[0] = 1
        for n in nums:
            curSum += n
            diff = curSum - goal

            res += pref[diff]
            pref[curSum] += 1

        return res