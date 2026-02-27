class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        count = defaultdict(int)
        res = 0
        
        l = 0
        for r in range(len(nums)):
            count[nums[r]] += 1
            while count[0] > 1:
                count[nums[l]] -= 1
                l += 1
            res = max(r - l + 1, res)
        return res - 1
