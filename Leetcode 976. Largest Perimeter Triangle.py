class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        i,j,k = 0,1,2
        perimeter = 0
        while k < len(nums):
            if (nums[i] + nums[j] > nums[k] and
                nums[i] + nums[k] > nums[j] and
                nums[j] + nums[k] > nums[i]):
                perimeter = nums[i] + nums[j] + nums[k]
                return perimeter
            i += 1
            j += 1
            k += 1
        return perimeter
