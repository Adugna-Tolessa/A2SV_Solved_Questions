class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i] != i + 1:
                idx = nums[i] - 1
                if nums[i] == nums[idx]:
                    return nums[i]
                nums[i], nums[idx] = nums[idx], nums[i]
            else:
                i += 1