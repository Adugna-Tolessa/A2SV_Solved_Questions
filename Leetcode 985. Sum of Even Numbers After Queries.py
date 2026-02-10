class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        evens = 0
        for n in nums:
            if n % 2 == 0:
                evens += n
        
        for i in range(len(queries)):
            prev = nums[queries[i][1]]
            nums[queries[i][1]] += queries[i][0]
            nxt = nums[queries[i][1]]
            if prev % 2 == 0:
                if nxt % 2 == 0:
                    evens += nxt - prev
                else:
                    evens -= prev
            else:
                if nxt % 2 == 0:
                    evens += nxt
            # temp = 0
            # for j in range(len(nums)):
            #     if nums[j] % 2 == 0:
            #         temp += nums[j]
            ans.append(evens)
        print(evens)
        return ans
