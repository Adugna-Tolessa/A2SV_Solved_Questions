class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums_freq = Counter(nums)
        ans = []
        n = len(nums)
        for key in nums_freq:
            if nums_freq[key] > (n//3):
                ans.append(key)
        return ans
