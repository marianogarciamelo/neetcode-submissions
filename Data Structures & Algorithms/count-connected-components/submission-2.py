class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        visited = set()
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(node):
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        res = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                res += 1
        return res

        