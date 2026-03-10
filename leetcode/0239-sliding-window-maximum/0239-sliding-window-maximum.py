class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = deque(nums[:k])
        max_win = 0
        ans = []
        stack = deque([])
        for i in range(k):
            # max_win = max(max_win, nums[i])
            while stack and stack[-1] < nums[i]:
                stack.pop()
            stack.append(nums[i])
        ans.append(stack[0])
        print(stack)
        for r in range(k, len(nums)):
            temp = window.popleft()
            window.append(nums[r])
            if temp == stack[0]:
                stack.popleft()
            while stack and stack[-1] < nums[r]:
                temp = stack.pop()
            stack.append(nums[r])
            ans.append(stack[0])
            # ans.append(max_win)
            # print(max_win)
            # break
        print(stack)
        return ans