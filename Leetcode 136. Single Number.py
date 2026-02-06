from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        store = Counter(nums)
        for num in nums:
            if store[num] == 1:
                return num
