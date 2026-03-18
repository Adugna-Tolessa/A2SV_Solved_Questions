class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        store = {}
        def score(l, r):
            if (l, r) in store:
                return store[l, r]
            if l > r:
                return 0
            a = nums[l] + min(score(l+1,r-1), score(l+2,r))
            b = nums[r] + min(score(l+1,r-1), score(l, r - 2))
            sc = max(a,b)
            store[l,r] = sc
            return sc
        p1 = score(0, len(nums) - 1)
        return p1 >= sum(nums) - p1