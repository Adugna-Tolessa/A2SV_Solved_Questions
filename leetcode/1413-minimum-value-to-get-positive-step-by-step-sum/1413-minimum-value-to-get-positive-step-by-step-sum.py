class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        curr= 0
        for i in range(len(nums)):
            curr += nums[i]
            nums[i] = curr
        n = min(nums)
        print(nums)
        if n >= 0:
            return 1
        else:
            return abs(n) + 1