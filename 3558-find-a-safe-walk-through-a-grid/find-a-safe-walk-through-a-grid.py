from collections import deque

class Solution(object):
    def findSafeWalk(self, grid, health):
        m = len(grid)
        n = len(grid[0])

        health -= grid[0][0]

        if health <= 0:
            return False

        q = deque([(0, 0, health)])

        best = [[-1] * n for _ in range(m)]
        best[0][0] = health

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while q:
            x, y, h = q.popleft()

            if x == m - 1 and y == n - 1:
                return True

            for dx, dy in directions:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < m and 0 <= ny < n:
                    nh = h - grid[nx][ny]

                    if nh > 0 and nh > best[nx][ny]:
                        best[nx][ny] = nh
                        q.append((nx, ny, nh))

        return False