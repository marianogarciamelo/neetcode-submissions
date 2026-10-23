class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        classMap = defaultdict(list)
        path = set()
        visited = set()

        for c, p in prerequisites:
            classMap[c].append(p)

        def dfs(cl):
            if cl in path:
                return False

            if cl in visited:
                return True

            path.add(cl)

            for prereq in classMap[cl]:
                if not dfs(prereq):
                    return False

            path.remove(cl)
            visited.add(cl)
            return True

        for cl in range(numCourses):
            if not dfs(cl):
                return False

        return True