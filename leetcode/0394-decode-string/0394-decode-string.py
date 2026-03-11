class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        # print("a".isalpha())
        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                temp = ""
                while stack and stack[-1] != "[":
                    temp = stack.pop() + temp
                stack.pop()
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                stack.append(int(num) * temp)
        return "".join(stack)
