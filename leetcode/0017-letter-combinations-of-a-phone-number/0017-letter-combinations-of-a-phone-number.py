class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        store = dig_letters = {"2":"abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        ans = []
        def backtrack(idx, s):
            if idx == len(digits):
                ans.append(s)
                return
            for n in store[digits[idx]]:
                s += n
                backtrack(idx + 1, s)
                s = s[: len(s) - 1]
        backtrack(0, "")
        return ans
