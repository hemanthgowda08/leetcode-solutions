class Solution(object):
    def maxBuilding(self, n, restrictions):
        restrictions.append([1, 0])
        restrictions.sort()

        m = len(restrictions)

        for i in range(1, m):
            restrictions[i][1] = min(
                restrictions[i][1],
                restrictions[i - 1][1] + restrictions[i][0] - restrictions[i - 1][0]
            )

        for i in range(m - 2, -1, -1):
            restrictions[i][1] = min(
                restrictions[i][1],
                restrictions[i + 1][1] + restrictions[i + 1][0] - restrictions[i][0]
            )

        ans = 0

        for i in range(m - 1):
            x1, h1 = restrictions[i]
            x2, h2 = restrictions[i + 1]

            dist = x2 - x1
            ans = max(ans, (h1 + h2 + dist) // 2)

        last_id, last_h = restrictions[-1]
        ans = max(ans, last_h + (n - last_id))

        return ans