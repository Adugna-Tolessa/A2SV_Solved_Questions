class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        i = 0
        while i < len(nums):
            idx = nums[i] - 1
            if i + 1 != nums[i]:
                if nums[i] == nums[idx]:
                    ans.append(nums[i])
                    i += 1
                else:
                    nums[idx], nums[i] = nums[i], nums[idx]
            else:
                i += 1
        return list(set(ans))