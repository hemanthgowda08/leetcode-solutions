from collections import deque

class Solution:
    def findMaxPathScore(self, edges, online, k):
        n = len(online)

        graph = [[] for _ in range(n)]
        indegree = [0] * n
        maxCost = 0

        for u, v, c in edges:
            graph[u].append((v, c))
            indegree[v] += 1
            maxCost = max(maxCost, c)

        # Topological order
        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        topo = []
        while q:
            u = q.popleft()
            topo.append(u)
            for v, _ in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)

        def check(limit):
            INF = 10**18
            dp = [INF] * n
            dp[0] = 0

            for u in topo:
                if dp[u] == INF:
                    continue

                if u != 0 and u != n - 1 and not online[u]:
                    continue

                for v, cost in graph[u]:
                    if cost < limit:
                        continue

                    if v != n - 1 and not online[v]:
                        continue

                    dp[v] = min(dp[v], dp[u] + cost)

            return dp[n - 1] <= k

        left, right = 0, maxCost
        ans = -1

        while left <= right:
            mid = (left + right) // 2

            if check(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans