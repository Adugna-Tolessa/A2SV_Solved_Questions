class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        store = {0:-1}
        pref = 0
        for i in range(len(nums)):
            pref += nums[i]
            r = pref % k
            if r in store and i - store[r] >= 2:
                return True
            elif r not in store:
                store[r] = i


        return False