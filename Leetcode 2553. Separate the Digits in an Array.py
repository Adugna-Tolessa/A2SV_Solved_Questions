class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            s = str(num)
            for n in s:
                ans.append(int(n))
        return ans
