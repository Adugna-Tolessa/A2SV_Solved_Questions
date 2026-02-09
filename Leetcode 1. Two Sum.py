class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = defaultdict(int)
        for i, n in enumerate(nums):
            diff = target - n
            if diff in temp:
                return [temp[diff], i]
            temp[n] = i
            

            
