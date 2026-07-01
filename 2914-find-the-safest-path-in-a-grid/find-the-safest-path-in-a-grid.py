from collections import deque

class Solution:
    def maximumSafenessFactor(self, grid):
        n = len(grid)
        dist = [[-1] * n for _ in range(n)]
        q = deque()
        d = [(1,0),(-1,0),(0,1),(0,-1)]

        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    dist[i][j] = 0
                    q.append((i,j))

        while q:
            x, y = q.popleft()
            for dx, dy in d:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

        def bfs(limit):
            if dist[0][0] < limit:
                return False

            q = deque([(0,0)])
            seen = {(0,0)}

            while q:
                x, y = q.popleft()
                if (x, y) == (n-1, n-1):
                    return True

                for dx, dy in d:
                    nx, ny = x + dx, y + dy
                    if (0 <= nx < n and 0 <= ny < n and
                        (nx, ny) not in seen and
                        dist[nx][ny] >= limit):
                        seen.add((nx, ny))
                        q.append((nx, ny))
            return False

        l, r = 0, max(map(max, dist))
        ans = 0

        while l <= r:
            mid = (l + r) // 2
            if bfs(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1

        return ans