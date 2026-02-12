class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n_count = Counter(nums)
        temp = sorted(nums, key = lambda a: -n_count[a])
        freq = temp[0]
        count = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == freq:
                n_count[freq] -= 1
                count += 1
                if count * 2 > i + 1:
                    print(n_count[freq])
                    if n_count[freq] * 2 > n - i - 1:
                        return i
                    # if nums[0] < nums[i]:
                    return -1

