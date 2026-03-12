class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        l = 0
        maxi = deque()
        mini = deque()
        ans = 0
        for r in range(len(nums)):
            while maxi and maxi[-1] < nums[r]:
                maxi.pop()
            while mini and mini[-1] > nums[r]:
                mini.pop()
            maxi.append(nums[r])
            mini.append(nums[r])
            while maxi[0] - mini[0] > limit:
                if nums[l] == maxi[0]:
                    maxi.popleft()
                if nums[l] == mini[0]:
                    mini.popleft()
                l += 1
            ans = max(ans, r - l + 1)
        return ans