class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        limit = nums[-1]
        ans = 0
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] <= limit:
                limit = nums[i]
            else:
                k = ceil(nums[i] / limit)
                ans += k - 1
                limit = nums[i] // k
            
        return ans