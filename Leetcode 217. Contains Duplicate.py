class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        store = Counter(nums)
        for key in store:
            if store[key] > 1:
                return True
        return False
