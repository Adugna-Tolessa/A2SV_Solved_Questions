class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        visited = [False] * len(graph)
        n = len(graph)
        target = n - 1
        path = []
        arr = []
        def dfs(node):
            if node not in arr:
                arr.append(node)
            if node == target:
                path.append(arr[:])
                return

            visited[node] = True
            for nei in graph[node]:
                if not visited[nei]:
                    dfs(nei)
                    arr.pop()
            visited[node] = False
        
        dfs(0)
        return path