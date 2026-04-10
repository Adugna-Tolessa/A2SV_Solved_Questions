class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        def backtrack(arr, idx):
            if len(arr) > 1:
                self.ans.append(arr[:])
            used = set()
            for i in range(idx, len(nums)):
                if nums[i] in used:
                    continue
                if not arr or arr[-1] <= nums[i]:
                    used.add(nums[i])
                    arr.append(nums[i])
                    backtrack(arr, i + 1)
                    arr.pop()

        backtrack([], 0)
        return self.ans