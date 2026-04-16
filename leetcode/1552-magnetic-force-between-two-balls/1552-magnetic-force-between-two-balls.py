class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        l, r = 1, position[-1] - position[0]
        ans = 0

        while l <= r:
            mid = (l + r) // 2

            lastPlaced = position[0]
            cnt = 1

            for i in range(1, len(position)):
                if position[i] - lastPlaced >= mid:
                    cnt += 1
                    lastPlaced = position[i]
                if cnt >= m:
                    break

            if cnt >= m:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1

        return ans