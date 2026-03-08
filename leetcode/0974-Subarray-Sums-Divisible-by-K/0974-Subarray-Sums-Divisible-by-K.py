class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        store = defaultdict(int)
        store[0] = 1
        pref = 0
        ans = 0
        for i in range(len(nums)):
            pref += nums[i]
            if pref % k in store:
                ans += store[pref % k]
            store[pref % k] += 1
        return ans