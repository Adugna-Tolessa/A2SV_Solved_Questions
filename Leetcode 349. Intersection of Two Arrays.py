class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_count = Counter(nums1)
        nums2_count = Counter(nums2)
        ans = []
        for key in nums1_count:
            if nums2_count[key]:
                ans.append(key)
        return ans
