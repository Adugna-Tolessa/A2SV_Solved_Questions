class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        graph = [set() for _ in range(n)]

        for i in range(n):
            x1, y1, r = bombs[i]
            for j in range(n):
                if i == j:
                    continue
                    
                x2, y2, r2 = bombs[j]
                diff = (x1 - x2) ** 2 + (y1 - y2) ** 2
                if r ** 2 >= diff:
                    graph[i].add(j)

        self.ans = 1

        def dfs(node, store, visited):
            if node in visited:
                return

            visited.add(node)
            store.add(node)
            self.ans = max(self.ans, len(store))

            for nei in graph[node]:
                dfs(nei, store, visited)

        for node in range(n):
            dfs(node, set(), set())

        return self.ans