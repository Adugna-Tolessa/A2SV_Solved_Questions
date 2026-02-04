class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        ans = []
        check = True      
        used = False      
        temp = ""

        for i in range(len(source)):
            j = 0
            if check:
                temp = ""
            while j < len(source[i]):
                if check and j + 1 < len(source[i]) and source[i][j:j+2] == "//":
                    break
                elif check and j + 1 < len(source[i]) and source[i][j:j+2] == "/*":
                    check = False
                    used = True
                    j += 2
                elif not check and j + 1 < len(source[i]) and source[i][j:j+2] == "*/":
                    check = True
                    used = False
                    j += 2
                elif check:
                    temp += source[i][j]
                    j += 1
                else:
                    j += 1
            if temp and check:
                ans.append(temp)
        return ans
