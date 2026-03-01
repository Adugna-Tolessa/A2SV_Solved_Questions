class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        store = defaultdict(int)
        ans = 0
        l_far = 0
        l_near = 0
        for r in range(len(nums)):
            store[nums[r]] += 1
            while len(store) > k:
                store[nums[l_near]] -= 1
                if store[nums[l_near]] == 0:
                    del store[nums[l_near]]
                l_near += 1
                l_far = l_near
            while store[nums[l_near]] > 1:
                store[nums[l_near]] -= 1
                l_near += 1
            if len(store) == k:
                ans += l_near - l_far + 1
        return ans
