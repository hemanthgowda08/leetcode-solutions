class Solution(object):
    def zigZagArrays(self, n, l, r):
        MOD = 10**9 + 7
        m = r - l + 1

        if n == 1:
            return m

        up = [0] * m
        down = [0] * m

        for i in range(m):
            up[i] = i
            down[i] = m - 1 - i

        for _ in range(3, n + 1):
            new_up = [0] * m
            new_down = [0] * m

            prefix_down = [0] * (m + 1)
            for i in range(m):
                prefix_down[i + 1] = (prefix_down[i] + down[i]) % MOD

            prefix_up = [0] * (m + 1)
            for i in range(m):
                prefix_up[i + 1] = (prefix_up[i] + up[i]) % MOD

            total_up = prefix_up[m]

            for i in range(m):
                new_up[i] = prefix_down[i]
                new_down[i] = (total_up - prefix_up[i + 1]) % MOD

            up = new_up
            down = new_down

        return (sum(up) + sum(down)) % MOD