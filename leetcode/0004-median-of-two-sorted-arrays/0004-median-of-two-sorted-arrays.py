class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = []
        l, r = 0, 0
        while l < len(nums1) and r < len(nums2):
            if nums1[l] <= nums2[r]:
                nums.append(nums1[l])
                l += 1
            else:
                nums.append(nums2[r])
                r += 1
        nums.extend(nums1[l:])
        nums.extend(nums2[r:])
        n = len(nums)
        if len(nums) % 2:
            return nums[n // 2]
        else:
            return (nums[n // 2 - 1] + nums[n // 2]) / 2 