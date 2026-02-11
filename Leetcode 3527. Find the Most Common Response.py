class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        store = defaultdict(int)
        ans = []
        for response in responses:
            temp = list(set(response))
            for t in temp:
                store[t] += 1
                if ans:
                    if ans[-1][0] < store[t]:
                        ans[-1] = [store[t], t]
                    elif ans[-1][0] == store[t]:
                        ans[-1][1] = min(ans[-1][1], t)
                else:
                    ans.append([store[t], t])
        print(store)
        return ans[-1][1]
            
