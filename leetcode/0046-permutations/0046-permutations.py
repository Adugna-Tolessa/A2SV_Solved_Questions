class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        store = []
        temp = [0] * len(nums)
        ans = []
        def backtrack(i):
            if len(store) == len(nums):
                ans.append(store[:])
                return

            for j in range(len(nums)):
                if temp[j]: continue
                temp[j] += 1
                store.append(nums[j])

                backtrack(i+1)
                
                store.pop()
                temp[j] -= 1
        backtrack(0)
        return ans