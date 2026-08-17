class Solution:
    def stoneGameV(self, stoneValue):
        n = len(stoneValue)
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        dp = [[-1] * n for _ in range(n)]

        def solve(i, j):
            if i >= j:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            ans = 0
            left = 0
            right = prefix[j + 1] - prefix[i]

            for k in range(i, j):
                left += stoneValue[k]
                right -= stoneValue[k]

                if left < right:
                    if ans >= left * 2:
                        continue
                    ans = max(ans, left + solve(i, k))

                elif left > right:
                    if ans >= right * 2:
                        break
                    ans = max(ans, right + solve(k + 1, j))

                else:
                    ans = max(
                        ans,
                        left + solve(i, k),
                        right + solve(k + 1, j)
                    )

            dp[i][j] = ans
            return ans

        return solve(0, n - 1)