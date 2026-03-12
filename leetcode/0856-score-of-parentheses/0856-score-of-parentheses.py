class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for i in range(len(s)):
            if s[i] == ")":
                temp = max(stack.pop() * 2, 1)
                stack[-1] += temp
            else:
                stack.append(0)
        return stack[-1]