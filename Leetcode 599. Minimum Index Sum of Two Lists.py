class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        temp = []
        check = True
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    if temp:
                        if temp[-1][0] == i + j:
                            temp.append([i + j, i, j])
                        else:
                            temp[-1] = min(temp[-1], [i + j, i, j])
                    else:
                        temp.append([i + j, i, j])
                    break
        ans = []
        for k in range(len(temp)):
            ans.append(list1[temp[k][1]])
        return ans
