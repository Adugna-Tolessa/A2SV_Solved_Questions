class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(first, arr, nums):
            ans.append(arr[:])
            for i in range(first, len(nums)):
                arr.append(nums[i])
                backtrack(i + 1, arr, nums)
                arr.pop()
        backtrack(0, [], nums)
        return ans