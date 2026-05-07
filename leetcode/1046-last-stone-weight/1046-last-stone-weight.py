class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapify(stones)
        while len(stones) > 1:
            first = -heappop(stones)
            second = -heappop(stones)
            if first > second:
                heappush(stones, second - first)
        if len(stones):
            return -heappop(stones)
        return 0