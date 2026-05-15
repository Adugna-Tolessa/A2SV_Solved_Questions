class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        heap = []

        for r in range(min(n, k)): 
            heappush(heap, (matrix[r][0], r, 0))

        for i in range(k - 1):
            val, r, c = heappop(heap)
            if c + 1 < n:
                heappush(heap, (matrix[r][c + 1], r, c + 1))
                
        return heap[0][0]