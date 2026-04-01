class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        
        def backtrack(first, arr, nums):
            ans.append(arr[:])
            for i in range(first, len(nums)):
                if i > first and nums[i] == nums[i - 1]:
                    continue
                
                arr.append(nums[i])
                backtrack(i + 1, arr, nums)
                arr.pop()
                
        backtrack(0, [], nums)
        return ans