class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2:
            return []

        store = Counter(changed)
        ans = []
        n = len(changed) // 2

        for num in sorted(changed):
            if store[num] == 0:
                continue

            if num == 0:
                if store[num] < 2:
                    return []
                store[num] -= 2
                ans.append(num)
            else:
                if store[num * 2] == 0:
                    return []
                store[num] -= 1
                store[num * 2] -= 1
                ans.append(num)

            if len(ans) == n:
                break

        if len(ans) == n:
            return ans  
        else:
            return []
