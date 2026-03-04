class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        pref = [0] * (len(nums) + 1)
        for req in requests:
            pref[req[0]] += 1
            pref[req[1] + 1] -= 1
        temp = 0
        for i in range(len(pref)):
            temp += pref[i]
            pref[i] = temp
        pref = pref[:-1]
        pref.sort(reverse = True)
        nums.sort(reverse = True)
        ans = 0
        for i in range(len(nums)):
            ans = (ans + nums[i] * pref[i]) % (10**9 + 7)
        return ans
