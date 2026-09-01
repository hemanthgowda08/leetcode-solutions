from collections import deque

class Solution(object):
    def minMoves(self, classroom, energy):
        m = len(classroom)
        n = len(classroom[0])

        litter = {}
        sr = 0
        sc = 0

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    sr = r
                    sc = c
                elif classroom[r][c] == 'L':
                    litter[(r, c)] = len(litter)

        count = len(litter)

        if count == 0:
            return 0

        target = (1 << count) - 1

        best = {}

        queue = deque()
        queue.append((sr, sc, energy, 0, 0))

        best[(sr, sc, 0)] = energy

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            r, c, e, mask, moves = queue.popleft()

            if mask == target:
                return moves

            if e == 0:
                continue

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue

                if classroom[nr][nc] == 'X':
                    continue

                ne = e - 1
                nmask = mask

                if classroom[nr][nc] == 'L':
                    nmask |= 1 << litter[(nr, nc)]

                if classroom[nr][nc] == 'R':
                    ne = energy

                state = (nr, nc, nmask)

                if state in best and best[state] >= ne:
                    continue

                best[state] = ne
                queue.append((nr, nc, ne, nmask, moves + 1))

        return -1