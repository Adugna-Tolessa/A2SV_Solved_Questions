class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        check = [0] * len(graph)
        def bfs(idx):
            if check[idx]:
                return True
            q = deque([idx])
            check[idx] = -1
            while q:
                idx = q.popleft()
                for neighbour in graph[idx]:
                    if check[idx] == check[neighbour]:
                        return False
                    elif not check[neighbour]:
                        q.append(neighbour)
                        check[neighbour] = -1 * check[idx]
            return True
        for i in range(len(graph)):
            if not bfs(i):
                return False
        return True