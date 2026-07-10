class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        arr = sorted((nums[i], i) for i in range(n))

        pos = [0] * n
        for i, (_, idx) in enumerate(arr):
            pos[idx] = i

        far = [0] * n
        j = 0
        for i in range(n):
            while j + 1 < n and arr[j + 1][0] - arr[i][0] <= maxDiff:
                j += 1
            far[i] = j

        LOG = 17
        up = [[0] * n for _ in range(LOG)]
        up[0] = far[:]

        for k in range(1, LOG):
            for i in range(n):
                up[k][i] = up[k - 1][up[k - 1][i]]

        ans = []

        for u, v in queries:
            if u == v:
                ans.append(0)
                continue

            pu = pos[u]
            pv = pos[v]

            if pu > pv:
                pu, pv = pv, pu

            if pu == pv:
                ans.append(0)
                continue

            if far[pu] == pu:
                ans.append(-1)
                continue

            steps = 0
            cur = pu

            for k in range(LOG - 1, -1, -1):
                if up[k][cur] < pv:
                    cur = up[k][cur]
                    steps += 1 << k

            if far[cur] >= pv:
                ans.append(steps + 1)
            else:
                ans.append(-1)

        return ans