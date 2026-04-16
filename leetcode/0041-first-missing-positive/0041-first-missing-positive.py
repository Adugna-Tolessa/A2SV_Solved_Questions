class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        while i < n:
            idx = nums[i] - 1
            if nums[i] <= 0:
                i += 1
            elif i + 1 != nums[i]:
                if idx < len(nums):
                    if nums[i] == nums[idx]:
                        i += 1
                    else:
                        nums[i], nums[idx] = nums[idx], nums[i]
                else:
                    i += 1
            else:
                i += 1
        next_num = 0
        for i in range(len(nums)):
            if i + 1 != nums[i]:
                return i + 1
            next_num = max(next_num, nums[i])
        return next_num + 1