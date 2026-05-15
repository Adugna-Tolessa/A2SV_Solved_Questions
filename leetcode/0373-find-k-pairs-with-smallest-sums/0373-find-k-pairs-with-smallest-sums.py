class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        h = []
        heapify(h)
        heappush(h, (nums1[0] + nums2[0], 0, 0))
        # for i in range(min(k, len(nums1))):
        #     for j in range(min(k, len(nums2))):
        #         heappush(h, [nums1[i] + nums2[j], i, j])
        ans = []
        visited = set()
        while h and k > 0:
            s, i, j = heappop(h)
            ans.append([nums1[i], nums2[j]])
            if j + 1 < len(nums2) and (i, j + 1) not in visited:
                visited.add((i, j + 1))
                heappush(h, (nums1[i] + nums2[j + 1], i, j + 1))
            if i + 1 < len(nums1) and (i + 1, j) not in visited:
                visited.add((i + 1, j))
                heappush(h, (nums1[i + 1] + nums2[j], i + 1, j))
            k -= 1
            
        return ans