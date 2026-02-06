class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        temp = []
        
        for _ in range(len(paths)):
            temp.append(paths[_].split())
        content = []
        temp2 = []

        for path in temp:
            for i in range(1,len(path)):
                j = len(path[i]) - 2
                while j > -1:
                    if path[i][j] == "(":
                        content.append(path[i][j + 1: len(path[i]) - 1])
                        temp2.append(path[0] + "/" + path[i][0:j])
                        break
                    j -= 1
        from collections import defaultdict
        directory = defaultdict(list)
        for c in range(len(content)):
            directory[content[c]].append(temp2[c])
        # print(directory)
        ans = []
        for a in directory.keys():
            if len(directory[a]) > 1:
                ans.append(directory[a])
        # print(content)
        # print(temp2)
        
        return ans
        
