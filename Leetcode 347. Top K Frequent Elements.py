class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # nums.sort()
        store = Counter(nums)
        ans = []
        i = 0
        for key in store:
            ans.append([store[key], key])
        temp = sorted(ans, reverse = True)
        res = []      
        for i in range(k):
            res.append(temp[i][1])
        return res
