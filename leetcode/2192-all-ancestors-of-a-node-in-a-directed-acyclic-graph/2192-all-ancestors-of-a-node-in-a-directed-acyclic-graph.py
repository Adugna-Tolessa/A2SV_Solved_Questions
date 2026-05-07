class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        inDegree = [0 for _ in range(n)]
        q = deque()

        for par, ch in edges:
            graph[par].append(ch)
            inDegree[ch] += 1

        for ch in range(n):
            if inDegree[ch] == 0:
                q.append(ch)

        temp = []
        while q:
            node = q.popleft()
            temp.append(node)
            for nei in graph[node]:
                inDegree[nei] -= 1
                if inDegree[nei] == 0:
                    q.append(nei)
        print(temp)
        res = [[] for _ in range(n)]
        ancestors = [set() for _ in range(n)]

        for node in temp:
            for nei in graph[node]:
                ancestors[nei].add(node)
                ancestors[nei].update(ancestors[node])

        for i in range(n):
            for node in range(n):
                if node == i:
                    continue
                if node in ancestors[i]:
                    res[i].append(node)

        return res