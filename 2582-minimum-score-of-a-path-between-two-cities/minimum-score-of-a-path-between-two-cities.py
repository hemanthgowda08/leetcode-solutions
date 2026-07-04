from collections import defaultdict

class Solution(object):
    def minScore(self, n, roads):
        graph = defaultdict(list)

        for u, v, d in roads:
            graph[u].append((v, d))
            graph[v].append((u, d))

        visited = set()
        ans = [float("inf")]

        def dfs(city):
            visited.add(city)

            for nei, dist in graph[city]:
                ans[0] = min(ans[0], dist)

                if nei not in visited:
                    dfs(nei)

        dfs(1)

        return ans[0]