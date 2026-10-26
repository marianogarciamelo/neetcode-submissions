
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for a, b in edges:  # Don't overwrite n
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        def dfs(node, parent):
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor == parent:  # 1. Skip the parent
                    continue

                if neighbor in visited:  # 2. Cycle detected
                    return False

                if not dfs(neighbor, node):  # 3. Propagate False
                    return False

            return True

        # 4. Check for cycles AND connectivity
        return dfs(0, -1) and len(visited) == n
