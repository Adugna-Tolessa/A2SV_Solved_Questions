class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff = sorted(costs, key=lambda x: x[0] - x[1])
        ans = 0
        for i in range(len(diff)//2):
            ans += diff[i][0]
        for i in range(len(diff)//2,len(diff)):
            ans += diff[i][1]
        return ans