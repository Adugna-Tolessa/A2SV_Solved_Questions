class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort(key=lambda x: x[1])

        count = 1
        store = points[0]

        for i in range(1, len(points)):
            if points[i][0] > store[1]:
                count += 1
                store = points[i]

        return count
            
