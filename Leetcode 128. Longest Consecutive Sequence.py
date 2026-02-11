class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)
        ans = 0
        for num in store: 
            if not num - 1 in store:
                i = 1
                while num + i in store:
                    i += 1
                ans = max(ans, i)
        return ans
