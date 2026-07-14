class Solution(object):
    def subsequencePairCount(self, nums):
        MOD = 1000000007
        mx = max(nums)

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        dp = [[0] * (mx + 1) for _ in range(mx + 1)]
        dp[0][0] = 1

        for num in nums:
            ndp = [row[:] for row in dp]
            for x in range(mx + 1):
                for y in range(mx + 1):
                    if dp[x][y] == 0:
                        continue

                    nx = gcd(x, num)
                    ndp[nx][y] = (ndp[nx][y] + dp[x][y]) % MOD

                    ny = gcd(y, num)
                    ndp[x][ny] = (ndp[x][ny] + dp[x][y]) % MOD

            dp = ndp

        ans = 0
        for g in range(1, mx + 1):
            ans = (ans + dp[g][g]) % MOD

        return ans